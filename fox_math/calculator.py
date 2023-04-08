import beaker
import pyteal as pt

app = beaker.Application("CalculatorApp")


@app.external
def add(a: pt.abi.Uint64, b: pt.abi.Uint64, *, output: pt.abi.Uint64) -> pt.Expr:
    """adds a to b"""
    return output.set(a.get() + b.get())

@app.external
def sub(a: pt.abi.Uint64, b: pt.abi.Uint64, *, output: pt.abi.Uint64) -> pt.Expr:
    """subtracts b from a"""
    return output.set(a.get() - b.get())
