from _typeshed import Self
from typing import Any, Callable, Dict, Text, Tuple, TypeVar

def run(statement: str, filename: str | None = ..., sort: str | int = ...) -> None: ...
def runctx(
    statement: str, globals: Dict[str, Any], locals: Dict[str, Any], filename: str | None = ..., sort: str | int = ...
) -> None: ...

_T = TypeVar("_T")
_Label = Tuple[str, int, str]

class Profile:
    bias: int
    stats: dict[_Label, tuple[int, int, int, int, dict[_Label, tuple[int, int, int, int]]]]  # undocumented
    def __init__(self, timer: Callable[[], float] | None = ..., bias: int | None = ...) -> None: ...
    def set_cmd(self, cmd: str) -> None: ...
    def simulate_call(self, name: str) -> None: ...
    def simulate_cmd_complete(self) -> None: ...
    def print_stats(self, sort: str | int = ...) -> None: ...
    def dump_stats(self, file: Text) -> None: ...
    def create_stats(self) -> None: ...
    def snapshot_stats(self) -> None: ...
    def run(self: Self, cmd: str) -> Self: ...
    def runctx(self: Self, cmd: str, globals: Dict[str, Any], locals: Dict[str, Any]) -> Self: ...
    def runcall(self, __func: Callable[..., _T], *args: Any, **kw: Any) -> _T: ...
    def calibrate(self, m: int, verbose: int = ...) -> float: ...
