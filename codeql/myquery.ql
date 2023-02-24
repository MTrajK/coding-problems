
import python
import CodeQL

from os import system

class OSCommandInjection extends CodeQL.Query {
  OSCommandInjection() {
    // Find all function calls to the Python 'os.system()' function
    // that pass a user-controlled string as an argument.
    // This is a potential command injection vulnerability.
    pythonScript("os_system_call.ql",
      """
      import python
      import DataFlow

      from os import system

      let userControlledString = pythonVariableAccess().getValue()
      fromExpr = DataFlow::exprToNode(userControlledString)
      osSystemCall = callExpr().getCallee() and osSystemFunc(osSystemCall)

      fromExpr.reaches(osSystemCall)
      and not osSystemCall.hasParameter(0,fromExpr)
      """)

    // Define the 'os.system()' function as a CodeQL predicate.
    osSystemFunc(FunctionCall fc) : fc.getTarget().getName() = "system" {}
  }
}

