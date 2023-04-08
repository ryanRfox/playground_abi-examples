import calculator
import select_math
import beaker


def demo() -> None:
    algod_client = beaker.sandbox.get_algod_client()
    account = beaker.sandbox.get_accounts().pop()

    # create a couple of clients for the same underlying application
    # definition
    first_app_client = beaker.client.ApplicationClient(
        algod_client,
        select_math.app,
        signer=account.signer,
    )

    second_app_client = beaker.client.ApplicationClient(
        algod_client,
        calculator.app,
        signer=account.signer,
    )

    # Deploy the apps on-chain
    first_app_client.create()
    second_app_client.create()

    # Set up our suggested params
    # to cover the fee for the inner transaction
    # that the app executes
    sp = algod_client.suggested_params()
    sp.fee = sp.min_fee * 2
    sp.flat_fee = True

    # Call the `add` method from the calculator app
    call_response = first_app_client.call(
        select_math.do_math,
        calculator_application=second_app_client.app_id,
        method=calculator.add.method_signature,
        a=1,
        b=2,
        suggested_params=sp,
    )
    print(call_response.return_value)


if __name__ == "__main__":
    demo()
