import python

from CallExpr call, Function f
where call.getTarget().toString() = "odd_sum" and
      call.getEnclosingFunction() = f
select f, call
