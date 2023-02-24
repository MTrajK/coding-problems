import python

from Function f, Parameter p
where p.is_variadic() and
      p.getDeclaringFunction() = f
select f, p
