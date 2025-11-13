
def func(param: int | str) -> int:
    if isinstance(param, int):
        return param
    elif isinstance(param, str):
        return len(param)

# In this case mypy understands that the if and elif cover all the valid options and does not complain about missing `return`
# If we remove the `elif` part we can see the mypy complaint.
# In another similar case in real code I saw it comlaining even when all the possibilities were handled.


class A:
    pass
class B:
    pass

def func2(param: A | B) -> int:
    if isinstance(param, A):
        return 1
    elif isinstance(param, B):
        return 2


