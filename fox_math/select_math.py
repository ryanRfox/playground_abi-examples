import beaker
import pyteal as pt
from typing import Literal

import calculator

app = beaker.Application("MathSelectionApp")

@app.external
def do_math(
    calculator_application: pt.abi.Application,
    calc_app_method_sig: pt.abi.String,
    # application_method: pt.abi.StaticBytes[Literal[4]],
    a: pt.abi.Uint64,
    b: pt.abi.Uint64,
    *,
    output: pt.abi.String, 
) -> pt.Expr:
    """calls the selected method from calculator app and returns the result"""
    return pt.Seq(
        # Call the selected method on the calculator application
        pt.InnerTxnBuilder.ExecuteMethodCall(
            app_id=calculator_application.application_id(),
            method_signature=calc_app_method_sig, # calculator.sub.method_signature(),
            args=[a,b],
            extra_fields={
                # Set the fee to 0 so we don't have to
                # fund the app account. We'll have to cover
                # the fee ourselves when we call this method
                # from off chain
                pt.TxnField.fee: pt.Int(0),
            },
        ),
        # Set the output to whatever it sent us back
        output.set(pt.Suffix(pt.InnerTxn.last_log(), pt.Int(4))),
    )
