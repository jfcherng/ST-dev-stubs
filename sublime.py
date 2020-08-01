# version: 4079

from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    overload,
    Sequence,
    Tuple,
    TypeVar,
    Union,
)
from typing_extensions import TypedDict


# ----- #
# types #
# ----- #

Layout = TypedDict(
    "Layout",
    # fmt: off
    {
        "cols": Sequence[float],
        "rows": Sequence[float],
        "cells": Sequence[Sequence[int]],
    },
    # fmt: on
)
Location = Tuple[str, str, Tuple[int, int]]
Point = int
Vector = Tuple[float, float]
Value = Union[dict, list, str, float, bool, None]

# fmt: off
T_completion = Union[
    str,
    Union[List[str], Tuple[str, str]],
    "CompletionItem",
]
# fmt: on

_T = TypeVar("_T")
Callback0 = Callable[[], None]
Callback1 = Callable[[_T], None]


# -------- #
# ST codes #
# -------- #

HOVER_TEXT: int = 1
HOVER_GUTTER: int = 2
HOVER_MARGIN: int = 3

ENCODED_POSITION: int = 1
TRANSIENT: int = 4
FORCE_GROUP: int = 8
ADD_TO_SELECTION_SEMI_TRANSIENT: int = 16
ADD_TO_SELECTION: int = 32
IGNORECASE: int = 2
LITERAL: int = 1
MONOSPACE_FONT: int = 1
KEEP_OPEN_ON_FOCUS_LOST: int = 2

HTML: int = 1
COOPERATE_WITH_AUTO_COMPLETE: int = 2
HIDE_ON_MOUSE_MOVE: int = 4
HIDE_ON_MOUSE_MOVE_AWAY: int = 8
KEEP_ON_SELECTION_MODIFIED: int = 16
HIDE_ON_CHARACTER_EVENT: int = 32

DRAW_EMPTY: int = 1
HIDE_ON_MINIMAP: int = 2
DRAW_EMPTY_AS_OVERWRITE: int = 4
PERSISTENT: int = 16
# Deprecated, use DRAW_NO_FILL instead
DRAW_OUTLINED: int = 32
DRAW_NO_FILL: int = 32
DRAW_NO_OUTLINE: int = 256
DRAW_SOLID_UNDERLINE: int = 512
DRAW_STIPPLED_UNDERLINE: int = 1024
DRAW_SQUIGGLY_UNDERLINE: int = 2048
NO_UNDO: int = 8192
HIDDEN: int = 128

OP_EQUAL: int = 0
OP_NOT_EQUAL: int = 1
OP_REGEX_MATCH: int = 2
OP_NOT_REGEX_MATCH: int = 3
OP_REGEX_CONTAINS: int = 4
OP_NOT_REGEX_CONTAINS: int = 5
CLASS_WORD_START: int = 1
CLASS_WORD_END: int = 2
CLASS_PUNCTUATION_START: int = 4
CLASS_PUNCTUATION_END: int = 8
CLASS_SUB_WORD_START: int = 16
CLASS_SUB_WORD_END: int = 32
CLASS_LINE_START: int = 64
CLASS_LINE_END: int = 128
CLASS_EMPTY_LINE: int = 256

INHIBIT_WORD_COMPLETIONS: int = 8
INHIBIT_EXPLICIT_COMPLETIONS: int = 16
DYNAMIC_COMPLETIONS: int = 32
INHIBIT_REORDER: int = 128

DIALOG_CANCEL: int = 0
DIALOG_YES: int = 1
DIALOG_NO: int = 2

UI_ELEMENT_SIDE_BAR: int = 1
UI_ELEMENT_MINIMAP: int = 2
UI_ELEMENT_TABS: int = 4
UI_ELEMENT_STATUS_BAR: int = 8
UI_ELEMENT_MENU: int = 16
UI_ELEMENT_OPEN_FILES: int = 32

LAYOUT_INLINE: int = 0
LAYOUT_BELOW: int = 1
LAYOUT_BLOCK: int = 2

KIND_ID_AMBIGUOUS: int = 0
KIND_ID_KEYWORD: int = 1
KIND_ID_TYPE: int = 2
KIND_ID_FUNCTION: int = 3
KIND_ID_NAMESPACE: int = 4
KIND_ID_NAVIGATION: int = 5
KIND_ID_MARKUP: int = 6
KIND_ID_VARIABLE: int = 7
KIND_ID_SNIPPET: int = 8

KIND_AMBIGUOUS: Tuple[int, str, str] = (KIND_ID_AMBIGUOUS, "", "")
KIND_KEYWORD: Tuple[int, str, str] = (KIND_ID_KEYWORD, "", "")
KIND_TYPE: Tuple[int, str, str] = (KIND_ID_TYPE, "", "")
KIND_FUNCTION: Tuple[int, str, str] = (KIND_ID_FUNCTION, "", "")
KIND_NAMESPACE: Tuple[int, str, str] = (KIND_ID_NAMESPACE, "", "")
KIND_NAVIGATION: Tuple[int, str, str] = (KIND_ID_NAVIGATION, "", "")
KIND_MARKUP: Tuple[int, str, str] = (KIND_ID_MARKUP, "", "")
KIND_VARIABLE: Tuple[int, str, str] = (KIND_ID_VARIABLE, "", "")
KIND_SNIPPET: Tuple[int, str, str] = (KIND_ID_SNIPPET, "s", "Snippet")

COMPLETION_FORMAT_TEXT: int = 0
COMPLETION_FORMAT_SNIPPET: int = 1
COMPLETION_FORMAT_COMMAND: int = 2

COMPLETION_FLAG_KEEP_PREFIX: int = 1


def version() -> str:
    """ Returns the version number """
    ...


def platform() -> str:
    """ Returns the platform, which may be "osx", "linux" or "windows" """
    ...


def arch() -> str:
    """ Returns the CPU architecture, which may be "x32" or "x64" """
    ...


def channel() -> str:
    """ Returns the release channel, which may be "stable" or "dev" """
    ...


def executable_path() -> str:
    """ Returns the path to the "sublime_text" executable """
    ...


def executable_hash() -> Tuple[str, str, str]:
    """
    Returns `(version_number, platform_arch, executable_hash)` such as

    ```python
    ('4079', 'windows_x64', '906388de50d5233b5648200ce9d1452a')
    ```
    """
    ...


def packages_path() -> str:
    """ Returns the path where all the user's loose packages are located """
    ...


def installed_packages_path() -> str:
    """ Returns the path where all the user's `.sublime-package` files are located """
    ...


def cache_path() -> str:
    """ Returns the path where Sublime Text stores cache files """
    ...


def status_message(msg: str) -> None:
    """ Shows a message in the status bar """
    ...


def error_message(msg: str) -> None:
    """ Displays an error dialog to the user """
    ...


def message_dialog(msg: str) -> None:
    """ Displays a message dialog to the user """
    ...


def ok_cancel_dialog(msg: str, ok_title: str = "") -> int:
    """
    Displays an <kbd>ok</kbd> <kbd>cancel</kbd> question dialog to the user If `ok_title` is
    provided, this may be used as the text on the <kbd>ok</kbd> button.
    Returns `True` if the user presses the <kbd>ok</kbd> button
    """
    ...


def yes_no_cancel_dialog(msg: str, yes_title: str = "", no_title: str = "") -> int:
    """
    Displays a <kbd>yes</kbd> <kbd>no</kbd> <kbd>cancel</kbd> question dialog to the user
    If `yes_title` and/or `no_title` are provided, they will be used as the
    text on the corresponding buttons on some platforms. Returns `DIALOG_YES`,
    `DIALOG_NO` or `DIALOG_CANCEL`
    """
    ...


def open_dialog(
    callback: Callable[[Optional[Union[str, List[str]]]], None],
    file_types: List[Tuple[str, List[str]]] = [],
    directory: Optional[str] = None,
    multi_select: bool = False,
    allow_folders: bool = False,
) -> None:
    """
    Shows the open file dialog.

    callback - Called with selected path or `None` once open dialog is closed.
    file_types: [(str, [str])] - A list of allowed file types, consisting of a
                                 description and a list of allowed extensions.
    directory: str | None - The directory the dialog should start in. Will use
                            the virtual working directory if not provided.
    multi_select: bool - Whether to allow selecting multiple files. Function
                         will call `callback` with a list if this is True.
    allow_folders: bool - Whether to also allow selecting folders. Only works on
                          macOS. If you only want to select folders use
                          `select_folder_dialog`.
    """
    ...


def save_dialog(
    callback: Callable[[Optional[str]], None],
    file_types: List[Tuple[str, List[str]]] = [],
    directory: Optional[str] = None,
    name: Optional[str] = None,
    extension: Optional[str] = None,
) -> None:
    """
    Shows the save file dialog.

    callback - Called with selected path or `None` once open dialog is closed.
    file_types: [(str, [str])] - A list of allowed file types, consisting of a
                                 description and a list of allowed extensions.
    directory: str | None - The directory the dialog should start in. Will use
                            the virtual working directory if not provided.
    name: str | None - The default name of the file in the save dialog.
    extension: str | None - The default extension used in the save dialog.
    """
    ...


def select_folder_dialog(
    callback: Callable[[Optional[Union[str, List[str]]]], None],
    directory: Optional[str] = None,
    multi_select: bool = False,
) -> None:
    """
    Show the select folder dialog.

    callback - Called with selected path or `None` once open dialog is closed.
    directory: str | None - The directory the dialog should start in. Will use
                            the virtual working directory if not provided.
    multi_select: bool - Whether to allow selecting multiple folders. Function
                         will call `callback` with a list if this is True.
    """
    ...


def run_command(cmd: str, args: Optional[Dict[str, Value]] = None) -> None:
    """ Runs the named `ApplicationCommand` with the (optional) given `args` """
    ...


def format_command(cmd: str, args: Optional[Dict[str, Value]] = None) -> str:
    """
    Creates a "command string" from a str cmd name, and an optional dict of args.
    This is used when constructing a command-based `CompletionItem`
    """
    ...


def html_format_command(cmd: str, args: Optional[Dict[str, Value]] = None) -> str:
    ...


def command_url(cmd: str, args: Optional[Dict[str, Value]] = None) -> str:
    """ Creates a `subl:` protocol URL for executing a command in a minihtml link """
    ...


def get_clipboard_async(callback: Callable[[str], None], size_limit: int = 16777216) -> None:
    """
    Calls `callback` with the contents of the clipboard. For performance reasons
    if the size of the clipboard content is bigger than `size_limit`, an empty
    string will be returned.
    """
    ...


def get_clipboard(size_limit: int = 16777216) -> str:
    """
    Warning: Deprecated in favor of `get_clipboard_async()`

    Returns the content of the clipboard. For performance reasons if the size of
    the clipboard content is bigger than size_limit, an empty string will be
    returned.
    """
    ...


def set_clipboard(text: str) -> None:
    """ Sets the contents of the clipboard """
    ...


def log_commands(flag: bool) -> None:
    """
    Controls command logging. If enabled, all commands run from key bindings
    and the menu will be logged to the console
    """
    ...


def log_input(flag: bool) -> None:
    """
    Enables or disables input logging. This is useful to find the names of
    certain keys on the keyboard
    """
    ...


def log_fps(flag: bool) -> None:
    """
    Enables or disables fps logging.
    """
    ...


def log_result_regex(flag: bool) -> None:
    """
    Enables or disables result regex logging. This is useful when trying to
    debug `file_regex` and `line_regex` in build systems
    """
    ...


def log_indexing(flag: bool) -> None:
    ...


def log_build_systems(flag: bool) -> None:
    ...


def log_control_tree(flag: bool) -> None:
    """
    When enabled, clicking with <kbd>Ctrl</kbd>+<kbd>Alt</kbd>
    will log the control tree under the mouse to the console.
    """
    ...


def score_selector(scope_name: str, selector: str) -> int:
    """
    Matches the `selector` against the given scope, returning a score
    A score of 0 means no match, above 0 means a match. Different selectors may
    be compared against the same scope: a higher score means the selector is a
    better match for the scope
    """
    ...


def load_resource(name: str) -> str:
    """
    Loads the given resource. The `name` should be in the format
    `Packages/Default/Main.sublime-menu`
    """
    ...


def load_binary_resource(name: str) -> bytes:
    """
    Loads the given resource. The `name` should be in the format
    `Packages/Default/Main.sublime-menu`
    """
    ...


def find_resources(pattern: str) -> List[str]:
    """ Finds resources whose file name matches the given `pattern` """
    ...


def encode_value(val: Value, pretty: bool = ...) -> str:
    """
    Encode a JSON compatible value into a string representation
    If `pretty` is set to `True`, the string will include newlines and indentation
    """
    ...


def decode_value(data: str) -> Value:
    """
    Decodes a JSON string into an object.
    If `data` is invalid, a `ValueError` will be thrown
    """
    ...


@overload
def expand_variables(val: str, variables: Dict[str, str]) -> str:
    """
    Expands any variables in the string `value` using the variables defined in
    the dictionary `variables`
    `value` may also be a `list` or `dict`, in which case the structure will be
    recursively expanded. Strings should use snippet syntax, for example:
    ```python
    expand_variables("Hello, ${name}", {"name": "Foo"})
    ```
    """
    ...


@overload
def expand_variables(val: List[str], variables: Dict[str, str]) -> List[str]:
    """
    Expands any variables in the string `value` using the variables defined in
    the dictionary `variables`
    `value` may also be a `list` or `dict`, in which case the structure will be
    recursively expanded. Strings should use snippet syntax, for example:
    ```python
    expand_variables("Hello, ${name}", {"name": "Foo"})
    ```
    """
    ...


@overload
def expand_variables(val: Dict[str, str], variables: Dict[str, str]) -> Dict[str, str]:
    """
    Expands any variables in the string `value` using the variables defined in
    the dictionary `variables`
    `value` may also be a `list` or `dict`, in which case the structure will be
    recursively expanded. Strings should use snippet syntax, for example:
    ```python
    expand_variables("Hello, ${name}", {"name": "Foo"})
    ```
    """
    ...


def list_syntaxes() -> List[Dict[str, Any]]:
    """
    Returns a list of all available syntaxes.
    Each dict will have the keys "path", "name", "hidden" and "scope"
    """
    ...


def find_syntax(fname: str, first_line: Optional[str] = None) -> Optional[str]:
    """
    Returns the path to the syntax that will be used when opening a file with the name fname.
    The first_line of file contents may also be provided if available.
    """
    ...


def load_settings(base_name: str) -> "Settings":
    """
    Loads the named settings. The name should include a file name and extension,
    but not a path The packages will be searched for files matching the
    `base_name`, and the results will be collated into the settings object
    Subsequent calls to `load_settings()` with the `base_name` will return the
    same object, and not load the settings from disk again
    """
    ...


def save_settings(base_name: str) -> None:
    """ Flushes any in-memory changes to the named settings object to disk """
    ...


def set_timeout(f: Callback0, timeout_ms: int = 0) -> None:
    """
    Schedules a function to be called in the future. Sublime Text will block
    while the function is running
    """
    ...


def set_timeout_async(f: Callback0, timeout_ms: int = 0) -> None:
    """
    Schedules a function to be called in the future. The function will be
    called in a worker thread, and Sublime Text will not block while the
    function is running
    """
    ...


def active_window() -> "Window":
    """ Returns the most recently used window """
    ...


def windows() -> "List[Window]":
    """ Returns a list of all the open windows """
    ...


def get_macro() -> List[Dict[str, Any]]:
    """
    Returns a list of the commands and args that compromise the currently recorded macro.
    Each dict will contain the keys "command" and "args".
    """
    ...


class Window:
    """ This class represents windows and provides an interface of methods to interact with them """

    window_id: int
    settings_object: "Optional[Settings]"
    template_settings_object: "Optional[Settings]"

    def __init__(self, id: int) -> None:
        ...

    def __eq__(self, other: Any) -> bool:
        ...

    def __bool__(self) -> bool:
        ...

    def __repr__(self) -> str:
        ...

    def id(self) -> int:
        """ Returns a number that uniquely identifies this window """
        ...

    def is_valid(self) -> bool:
        """ 
        Returns true if the `Window` is still a valid handle. 
        Will return False for a closed window, for example. 
        """
        ...

    def hwnd(self) -> int:
        """ Platform specific window handle, only returns a meaningful result under Windows """
        ...

    def active_sheet(self) -> "Optional[Sheet]":
        """ Returns the currently focused sheet """
        ...

    def active_view(self) -> "Optional[View]":
        """ Returns the currently edited view """
        ...

    def new_html_sheet(self, name: str, contents: str, flags: int = 0, group: int = -1) -> "Sheet":
        """
        Constructs a sheet with HTML contents rendered using minihtml.

        name: A unicode string of the sheet name, shown in tab and Open Files

        contents: A unicode string of the HTML contents

        flags: A bitwise combination of:
        `sublime.TRANSIENT`: If the sheet should be transient
        `sublime.ADD_TO_SELECTION`: Add the file to the currently selected sheets in this group

        group: An integer of the group to add the sheet to, -1 for the active group
        """
        ...

    def run_command(self, cmd: str, args: Optional[Dict[str, Value]] = ...) -> None:
        """
        Runs the named `WindowCommand` with the (optional) given `args`
        This method is able to run any sort of command, dispatching the
        command via input focus
        """
        ...

    def new_file(self, flags: int = 0, syntax: str = "") -> "View":
        """
        Creates a new file, The returned view will be empty, and its
        `is_loaded()` method will return `True`. Flags must be either `0` or `TRANSIENT`
        """
        ...

    def open_file(self, fname: str, flags: int = 0, group: int = -1) -> "View":
        """
        Opens the named file, and returns the corresponding view. If the file is
        already opened, it will be brought to the front. Note that as file
        loading is asynchronous, operations on the returned view won't be
        possible until its `is_loading()` method returns `False`.

        The optional `flags` parameter is a bitwise combination of:

        `ENCODED_POSITION`: Indicates the file_name should be searched for
        a :row or :row:col suffix
        `TRANSIENT`: Open the file as a preview only: it won't have a tab
        assigned it until modified
        `FORCE_GROUP`: don't select the file if it's opened in a different group
        """
        ...

    def find_open_file(self, fname: str) -> "Optional[View]":
        """
        Finds the named file in the list of open files, and returns the
        corresponding `View`, or `None` if no such file is open
        """
        ...

    def num_groups(self) -> int:
        """ Returns the number of view groups in the window """
        ...

    def active_group(self) -> int:
        """ Returns the index of the currently selected group """
        ...

    def focus_group(self, idx: int) -> None:
        """ Makes the given group active """
        ...

    def focus_sheet(self, sheet: "Sheet") -> None:
        """ Switches to the given `sheet` """
        ...

    def focus_view(self, view: "View") -> None:
        """ Switches to the given `view` """
        ...

    def bring_to_front(self) -> None:
        """ Brings the window in front of any other windows """
        ...

    def get_sheet_index(self, sheet: "Sheet") -> Tuple[int, int]:
        """
        Returns the group, and index within the group of the `sheet`
        Returns (-1, -1) if not found
        """
        ...

    def get_view_index(self, view: "View") -> Tuple[int, int]:
        """
        Returns the group, and index within the group of the `view`
        Returns (-1, -1) if not found
        """
        ...

    def set_sheet_index(self, sheet: "Sheet", group: int, idx: int) -> None:
        """ Moves the `sheet` to the given `group` and index """
        ...

    def set_view_index(self, view: "View", group: int, idx: int) -> None:
        """ Moves the `view` to the given `group` and index """
        ...

    def sheets(self) -> "List[Sheet]":
        """ Returns all open sheets in the window """
        ...

    def views(self) -> "List[View]":
        """ Returns all open views in the window """
        ...

    def active_sheet_in_group(self, group: int) -> "Optional[Sheet]":
        """ Returns the currently focused sheet in the given `group` """
        ...

    def active_view_in_group(self, group: int) -> "Optional[View]":
        """ Returns the currently edited view in the given `group` """
        ...

    def sheets_in_group(self, group: int) -> "List[Sheet]":
        """ Returns all open sheets in the given `group` """
        ...

    def views_in_group(self, group: int) -> "List[View]":
        """ Returns all open views in the given `group` """
        ...

    def transient_sheet_in_group(self, group: int) -> "Optional[Sheet]":
        """ Returns the transient `Sheet` in the given `group` if any """
        ...

    def transient_view_in_group(self, group: int) -> "Optional[View]":
        """ Returns the transient `View` in the given `group` if any """
        ...

    def layout(self) -> Layout:
        """ Returns the current layout """
        ...

    def get_layout(self) -> Layout:
        """ Deprecated, use `layout()` """
        ...

    def set_layout(self, layout: Layout) -> None:
        """ Changes the tile-based panel layout of view groups """
        ...

    def create_output_panel(self, name: str, unlisted: bool = False) -> "View":
        """
        Returns the view associated with the named output panel, creating it if required
        The output panel can be shown by running the _show_panel_ window command,
        with the panel argument set to the `name` with an "output." prefix.

        The optional `unlisted` parameter is a boolean to control if the
        output panel should be listed in the panel switcher
        """
        ...

    def find_output_panel(self, name: str) -> "Optional[View]":
        """
        Returns the view associated with the named output panel, or `None` if
        the output panel does not exist
        """
        ...

    def destroy_output_panel(self, name: str) -> None:
        """ Destroys the named output panel, hiding it if currently open """
        ...

    def active_panel(self) -> Optional[str]:
        """
        Returns the name of the currently open panel, or `None` if no panel is open
        Will return built-in panel names (e.g. "console", "find", etc)
        in addition to output panels
        """
        ...

    def panels(self) -> List[str]:
        """
        Returns a list of the names of all panels that have not been marked as unlisted
        Includes certain built-in panels in addition to output panels
        """
        ...

    def get_output_panel(self, name: str) -> "View":
        """ deprecated, use `create_output_panel()` """
        ...

    def show_input_panel(
        self,
        caption: str,
        initial_text: str,
        on_done: Optional[Callback1[str]],
        on_change: Optional[Callback1[str]],
        on_cancel: Callback0,
    ) -> "View":
        """
        Shows the input panel, to collect a line of input from the user
        `on_done` and `on_change`, if not `None`, should both be functions
        that expect a single string argument
        `on_cancel` should be a function that expects no arguments
        The view used for the input widget is returned
        """
        ...

    def show_quick_panel(
        self,
        items: Union[Sequence[str], Sequence[Sequence[str]]],
        on_select: Callback1[int],
        flags: int = 0,
        selected_index: int = -1,
        on_highlight: Optional[Callback1[int]] = None,
    ) -> None:
        """
        Shows a quick panel, to select an item in a list.

        * `items` may be a list of strings, or a list of string lists
        In the latter case, each entry in the quick panel will show multiple rows.

        * `on_select` will be called once, with the index of the selected item
        If the quick panel was cancelled, `on_select` will be called with an
        argument of `-1`.

        * `flags` is a bitwise OR of `MONOSPACE_FONT`
        and `KEEP_OPEN_ON_FOCUS_LOST`

        * `on_highlighted`, if given, will be called every time the highlighted item in the quick panel is changed
        """
        ...

    def is_sidebar_visible(self) -> bool:
        """ Returns `True` if the sidebar will be shown when contents are available """
        ...

    def set_sidebar_visible(self, flag: bool) -> None:
        """ Sets the sidebar to be shown or hidden when contents are available """
        ...

    def is_minimap_visible(self) -> bool:
        """ Returns `True` if the minimap is enabled """
        ...

    def set_minimap_visible(self, flag: bool) -> None:
        """ Controls the visibility of the minimap """
        ...

    def is_status_bar_visible(self) -> bool:
        """ Returns `True` if the status bar will be shown """
        ...

    def set_status_bar_visible(self, flag: bool) -> None:
        """ Controls the visibility of the status bar """
        ...

    def get_tabs_visible(self) -> bool:
        """ Returns `True` if tabs will be shown for open files """
        ...

    def set_tabs_visible(self, flag: bool) -> None:
        """ Controls if tabs will be shown for open files """
        ...

    def is_menu_visible(self) -> bool:
        """ Returns `True` if the menu is visible """
        ...

    def set_menu_visible(self, flag: bool) -> None:
        """ Controls if the menu is visible """
        ...

    def folders(self) -> List[str]:
        """ Returns a list of the currently open folders """
        ...

    def project_file_name(self) -> str:
        """ Returns name of the currently opened project file, if any """
        ...

    def project_data(self) -> Optional[Dict[str, Value]]:
        """
        Returns the project data associated with the current window
        The data is in the same format as the contents of a _.sublime-project_ file
        """
        ...

    def set_project_data(self, v: Dict[str, Value]) -> None:
        """
        Updates the project data associated with the current window
        If the window is associated with a _.sublime-project_ file, the project
        file will be updated on disk, otherwise the window will store the data
        internally
        """
        ...

    def workspace_file_name(self) -> Optional[str]:
        """ Returns the workspace filename of the current `Window` if possible """
        ...

    def settings(self) -> "Settings":
        """ Per-window settings, the contents are persisted in the session """
        ...

    def template_settings(self) -> "Settings":
        """
        Per-window settings that are persisted in the session, and duplicated
        into new windows
        """
        ...

    def lookup_symbol_in_index(self, sym: str) -> List[Location]:
        """ Finds all files and locations where sym is defined, using the symbol index """
        ...

    def lookup_symbol_in_index_by_kind(self, sym: str, kind: int) -> List[Location]:
        """ Finds all files and locations where sym is defined, using the symbol index """
        ...

    def lookup_symbol_in_open_files(self, sym: str) -> List[Location]:
        """
        Returns all files and locations where the symbol `sym` is defined, searching
        through open files
        """
        ...

    def lookup_symbol_in_open_files_by_kind(self, sym: str, kind: int) -> List[Location]:
        """ Finds all files and locations where sym is defined, searching through open files """
        ...

    def lookup_references_in_index(self, sym: str) -> List[Location]:
        """
        Returns all files and locations where the symbol `sym` is referenced,
        using the symbol index
        """
        ...

    def lookup_references_in_open_files(self, sym: str) -> List[Location]:
        """
        Returns all files and locations where the symbol `sym` is referenced,
        searching through open files
        """
        ...

    def extract_variables(self) -> Dict[str, str]:
        """
        Returns a dictionary of strings populated with contextual keys:
        `packages`, `platform`, `file`, `file_path`, `file_name`, `file_base_name`,
        `file_extension`, `folder`, `project`, `project_path`, `project_name`,
        `project_base_name`, `project_extension`
        This dict is suitable for passing to `sublime.expand_variables()`
        """
        ...

    def status_message(self, msg: str) -> None:
        """ Show a message in the status bar """
        ...


class Edit:
    """
    `Edit` objects have no functions, they exist to group buffer modifications

    `Edit` objects are passed to `TextCommands`, and can not be created by the
    user. Using an invalid `Edit` object, or an `Edit` object from a different view,
    will cause the functions that require them to fail
    """

    edit_token: int

    def __init__(self, token: int) -> None:
        ...

    def __repr__(self) -> str:
        ...


class Region:
    """ Represents an area of the buffer. Empty regions, where `a == b` are valid """

    a: int
    b: int
    xpos: int

    def __init__(self, a: int, b: Optional[int] = None, xpos: int = -1) -> None:
        ...

    def __iter__(self) -> Iterator:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def __len__(self) -> int:
        ...

    def __eq__(self, rhs: Any) -> bool:
        ...

    def __hash__(self) -> int:
        ...

    def __lt__(self, rhs: "Region") -> bool:
        ...

    def __contains__(self, v: Union["Region", Point]) -> bool:
        ...

    def to_tuple(self) -> Tuple[Point, Point]:
        """ Returns a tuple of this region (excluding xpos).

        Use this to uniquely identify a region in a set or similar. Regions
        can't be used for that directly as they may be mutated.
        """
        ...

    def empty(self) -> bool:
        """ Returns `True` if `begin() == end()` """
        ...

    def begin(self) -> int:
        """ Returns the minimum of `a` and `b` """
        ...

    def end(self) -> int:
        """ Returns the maximum of `a` and `b` """
        ...

    def size(self) -> int:
        """
        deprecated, use `len()` instead
        Returns the number of characters spanned by the region. Always >= 0
        """
        ...

    def contains(self, x: Union["Region", Point]) -> bool:
        """
        If `x` is a region, returns `True` if it's a subset
        If `x` is a point, returns `True` if `begin() <= x <= end()`
        """
        ...

    def cover(self, rhs: "Region") -> "Region":
        """ Returns a `Region` spanning both this and the given regions """
        ...

    def intersection(self, rhs: "Region") -> "Region":
        """ Returns the set intersection of the two regions """
        ...

    def intersects(self, rhs: "Region") -> bool:
        """
        Returns `True` if `self == rhs` or both include one or more
        positions in common
        """
        ...


class HistoricPosition:
    """
    Provides a snapshot of the row and column info for a point, before changes were made to a `View`.
    This is primarily useful for replaying changes to a document.
    """

    pt: Point
    row: int
    col: int
    col_utf16: int
    col_utf8: int

    def __init__(self, pt: Point, row: int, col: int, col_u16: int, col_u8: int) -> None:
        ...

    def __repr__(self) -> str:
        ...


class TextChange:
    """
    Represents a change that occured to the text of a `View`.
    This is primarily useful for replaying changes to a document.
    """

    a: HistoricPosition
    b: HistoricPosition
    len_utf16: int
    len_utf8: int
    str: str

    def __init__(self, pa: HistoricPosition, pb: HistoricPosition, s: str) -> None:
        ...

    def __repr__(self) -> str:
        ...


class Selection:
    """
    Maintains a set of Regions, ensuring that none overlap
    The regions are kept in sorted order
    """

    view_id: int

    def __init__(self, id: int) -> None:
        ...

    def __iter__(self) -> Iterator:
        ...

    def __len__(self) -> int:
        ...

    def __getitem__(self, index: int) -> Region:
        ...

    def __delitem__(self, index: int) -> None:
        ...

    def __eq__(self, rhs: Any) -> bool:
        ...

    def __lt__(self, rhs: "Selection") -> bool:
        ...

    def __bool__(self) -> bool:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def is_valid(self) -> bool:
        """ Determines if this `Selection` object is still valid """
        ...

    def clear(self) -> None:
        """ Removes all regions """
        ...

    def add(self, x: Union[Region, Point]) -> None:
        """
        Adds the given region or point. It will be merged with any intersecting
        regions already contained within the set
        """
        ...

    def add_all(self, regions: Sequence[Union[Region, Point]]) -> None:
        """ Adds all `regions` in the given list or tuple """
        ...

    def subtract(self, region: Region) -> None:
        """ Subtracts the `region` from all regions in the set """
        ...

    def contains(self, region: Region) -> None:
        """
        Deprecated, use `in` instead.

        Returns `True` if the given `region` is a subset
        """
        ...


def make_sheet(sheet_id: int) -> "Sheet":
    """ Create a `Sheet` object with the given ID """


class Sheet:
    """
    Represents a content container, i.e. a tab, within a window
    Sheets may contain a View, or an image preview
    """

    sheet_id: int

    def __init__(self, id: int) -> None:
        ...

    def __eq__(self, other: Any) -> bool:
        ...

    def __repr__(self) -> str:
        ...

    def id(self) -> int:
        """ Returns a number that uniquely identifies this sheet """
        ...

    def window(self) -> Optional[Window]:
        """
        Returns the window containing the sheet. May be `None` if the sheet
        has been closed
        """
        ...

    def view(self) -> "Optional[View]":
        """
        Returns the view contained within the sheet. May be `None` if the
        sheet is an image preview, or the view has been closed
        """
        ...

    def file_name(self) -> Optional[str]:
        """
        The full name file the file associated with the buffer,
        or None if it doesn't exist on disk.
        """
        ...


class TextSheet(Sheet):
    sheet_id: int

    def __init__(self, id: int) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def set_name(self, name: str) -> None:
        """ Sets the name of this `Sheet` """
        ...


class ImageSheet(Sheet):
    sheet_id: int

    def __repr__(self) -> str:
        ...


class HtmlSheet(Sheet):
    sheet_id: int

    def __init__(self, id: int) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def set_name(self, name: str) -> None:
        """ Sets the name of this `Sheet` """
        ...

    def set_contents(self, contents: str) -> None:
        """ Sets the content of this `Sheet` """
        ...


class View:
    """
    Represents a view into a text buffer. Note that multiple views may refer to
    the same buffer, but they have their own unique selection and geometry
    """

    view_id: int
    selection: Selection
    settings_object: "Settings"

    def __init__(self, id: int) -> None:
        ...

    def __len__(self) -> int:
        ...

    def __eq__(self, other: Any) -> bool:
        ...

    def __bool__(self) -> bool:
        ...

    def __repr__(self) -> str:
        ...

    def id(self) -> int:
        """ Returns a number that uniquely identifies this view """
        ...

    def buffer_id(self) -> int:
        """ Returns a number that uniquely identifies the buffer underlying this view """
        ...

    def element(self) -> Optional[str]:
        """
        Returns None for normal views, for views that comprise part of the UI, 
        a str is returned from the following list:

        "console:input": The console input

        "goto_anything:input": The input for the Goto Anything

        "command_palette:input": The input for the Command Palette

        "find:input": The input for the Find panel

        "incremental_find:input": The input for the Incremental Find panel

        "replace:input:find": The Find input for the Replace panel

        "replace:input:replace": The Replace input for the Replace panel

        "find_in_files:input:find": The Find input for the Find in Files panel

        "find_in_files:input:location": The Where input for the Find in Files panel

        "find_in_files:input:replace": The Replace input for the Find in Files panel

        "find_in_files:output": The output panel for Find in Files (buffer or output panel)

        "input:input": The input for the Input panel

        "exec:output": The output for the exec command

        "output:output": A general output panel

        The console output, indexer status output and license input controls 
        are not accessible via the API.
        """
        ...

    def is_valid(self) -> bool:
        """ 
        Returns true if the View is still a valid handle. 
        Will return False for a closed view, for example. 
        """
        ...

    def is_primary(self) -> bool:
        """
        Returns `True` if the view is the primary view into a file
        Will only be `False` if the user has opened multiple views into a file
        """
        ...

    def window(self) -> Optional[Window]:
        """ Returns a reference to the window containing the view """
        ...

    def file_name(self) -> Optional[str]:
        """
        The full name file the file associated with the buffer, or `None` if it
        doesn't exist on disk
        """
        ...

    def close(self) -> bool:
        """ Closes this view """
        ...

    def retarget(self, new_fname: str) -> None:
        ...

    def name(self) -> str:
        """ The name assigned to the buffer, if any """
        ...

    def set_name(self, name: str) -> None:
        """ Assigns a `name` to the buffer """
        ...

    def reset_reference_document(self) -> None:
        ...

    def set_reference_document(self, reference: str) -> None:
        ...

    def is_loading(self) -> bool:
        """
        Returns `True` if the buffer is still loading from disk,
        and not ready for use
        """
        ...

    def is_dirty(self) -> bool:
        """ Returns `True` if there are any unsaved modifications to the buffer """
        ...

    def is_read_only(self) -> bool:
        """ Returns `True` if the buffer may not be modified """
        ...

    def set_read_only(self, read_only: bool) -> None:
        """ Sets the read only property on the buffer """
        ...

    def is_scratch(self) -> bool:
        """
        Returns `True` if the buffer is a scratch buffer. Scratch buffers
        never report as being dirty
        """
        ...

    def set_scratch(self, scratch: bool) -> None:
        """
        Sets the scratch flag on the text buffer. When a modified scratch buffer
        is closed, it will be closed without prompting to save.
        """
        ...

    def encoding(self) -> str:
        """ Returns the encoding currently associated with the file """
        ...

    def set_encoding(self, encoding_name: str) -> None:
        """ Applies a new encoding to the file. This encoding will be used the
        next time the file is saved """
        ...

    def line_endings(self) -> str:
        """ Returns the line endings used by the current file """
        ...

    def set_line_endings(self, line_ending_name: str) -> None:
        """ Sets the line endings that will be applied when next saving """
        ...

    def size(self) -> int:
        """
        Deprecated, use `len()` instead.

        Returns the number of character in the file
        """
        ...

    def begin_edit(
        self, edit_token: int, cmd: str, args: Optional[Dict[str, Value]] = None
    ) -> Edit:
        ...

    def end_edit(self, edit: Edit) -> None:
        ...

    def is_in_edit(self) -> bool:
        ...

    def insert(self, edit: Edit, pt: Point, text: str) -> int:
        """
        Inserts the given string in the buffer at the specified point
        Returns the number of characters inserted, this may be different if
        tabs are being translated into spaces in the current buffer
        """
        ...

    def erase(self, edit: Edit, r: Region) -> None:
        """ Erases the contents of the region from the buffer """
        ...

    def replace(self, edit: Edit, r: Region, text: str) -> None:
        """ Replaces the contents of the region with the given string """
        ...

    def change_count(self) -> int:
        """
        Returns the current change count. Each time the buffer is modified,
        the change count is incremented. The change count can be used to
        determine if the buffer has changed since the last it was inspected
        """
        ...

    def change_id(self) -> Tuple[int, int, int]:
        """
        Returns a 3-element tuple that can be passed to `transform_region_from()`
        to obtain a region equivalent to a region of the View in the past.
        This is primarily useful for plugins providing text modification that
        must operate in an asynchronous fashion and must be able to handle the
        view contents changing between the request and response.
        """
        ...

    def transform_region_from(self, r: Region, change_id: Tuple[int, int, int]) -> Region:
        """
        Transforms a region from a previous point in time to an equivalent
        region in the current state of the View. The `change_id` must have been
        obtained from `change_id()` at the point in time the region is from.
        """
        ...

    def run_command(self, cmd: str, args: Optional[Dict[str, Value]] = None) -> None:
        """ Runs the named `TextCommand` with the (optional) given `args` """
        ...

    def sel(self) -> Selection:
        """ Returns a reference to the selection """
        ...

    def substr(self, x: Union[Region, Point]) -> str:
        """
        if `x` is a region, returns it's contents as a string
        if `x` is a point, returns the character to it's right
        """
        ...

    def find(self, pattern: str, start_pt: int, flags: int = 0) -> Optional[Region]:
        """
        Returns the first region matching the regex `pattern`, starting from
        `start_pt`, or `None` if it can't be found. The optional `flags`
        parameter may be `LITERAL`, `IGNORECASE`, or the two
        ORed together
        """
        ...

    def find_all(
        self,
        pattern: str,
        flags: int = 0,
        fmt: Optional[str] = None,
        extractions: Optional[List[str]] = None,
    ) -> List[Vector]:
        """
        Returns all (non-overlapping) regions matching the regex `pattern`
        The optional `flags` parameter may be `LITERAL`,
        `IGNORECASE`, or the two ORed together. If a format string is
        given, then all matches will be formatted with the formatted string
        and placed into the `extractions` list
        """
        ...

    def settings(self) -> "Settings":
        """
        Returns a reference to the view's settings object. Any changes to this
        settings object will be private to this view
        """
        ...

    def meta_info(self, key: str, pt: Point) -> str:
        ...

    def extract_tokens_with_scopes(self, r: Region) -> List[Tuple[Vector, str]]:
        """
        Gets the scope information for the given region.

        The returned value is like
        ```python
        [(Region(0, 6), 'source.python meta.statement...')]
        ```
        """
        ...

    def extract_scope(self, pt: Point) -> Region:
        """
        Returns the extent of the syntax scope name assigned to the
        character at the given point
        """
        ...

    def scope_name(self, pt: Point) -> str:
        """ Returns the syntax scope name assigned to the character at the given point """
        ...

    def match_selector(self, pt: Point, selector: str) -> bool:
        """
        Checks the `selector` against the scope at the given point
        returning a bool if they match
        """
        ...

    def score_selector(self, pt: Point, selector: str) -> int:
        """
        Matches the `selector` against the scope at the given point, returning a score
        A score of 0 means no match, above 0 means a match. Different selectors may
        be compared against the same scope: a higher score means the selector
        is a better match for the scope
        """
        ...

    def find_by_selector(self, selector: str) -> List[Region]:
        """
        Finds all regions in the file matching the given `selector`,
        returning them as a list
        """
        ...

    def style(self) -> Dict[str, str]:
        """
        Returns a dict of the global style settings for the view
        All colors are normalized to the six character hex form with
        a leading hash, e.g. _#ff0000_
        """
        ...

    def style_for_scope(self, scope: str) -> Dict[str, Any]:
        """
        Accepts a string `scope` and returns a dict of style information,
        include the keys _foreground_, _bold_, _italic_, _source_line_,
        _source_column_ and _source_file_.
        If the `scope` has a background color set, the key _background_ will
        be present. The foreground and background colors are normalized to the
        six character hex form with a leading hash, e.g. _#ff0000_
        """
        ...

    def indented_region(self, pt: Point) -> Region:
        ...

    def indentation_level(self, pt: Point) -> int:
        ...

    def has_non_empty_selection_region(self) -> bool:
        """ Determines if there is a non empty selection region in this view """
        ...

    def lines(self, r: Region) -> List[Region]:
        """ Returns a list of lines (in sorted order) intersecting the region `r` """
        ...

    def split_by_newlines(self, r: Region) -> List[Region]:
        """Splits the region up such that each region returned exists on
        exactly one line"""
        ...

    def line(self, x: Union[Region, Point]) -> Region:
        """
        if `x` is a region, returns a modified copy of region such that it
        starts at the beginning of a line, and ends at the end of a line
        Note that it may span several lines
        if `x` is a point, returns the line that contains the point
        """
        ...

    def full_line(self, x: Union[Region, Point]) -> Region:
        """ As line(), but the region includes the trailing newline character, if any """
        ...

    def word(self, x: Union[Region, Point]) -> Region:
        """
        if `x` is a region, returns a modified copy of it such that it
        starts at the beginning of a word, and ends at the end of a word
        Note that it may span several words
        if `x` is a point, returns the word that contains it
        """
        ...

    def classify(self, pt: Point) -> int:
        """
        Classifies the point `pt`, returning a bitwise OR of zero or more of these flags:
        `CLASS_WORD_START`
        `CLASS_WORD_END`
        `CLASS_PUNCTUATION_START`
        `CLASS_PUNCTUATION_END`
        `CLASS_SUB_WORD_START`
        `CLASS_SUB_WORD_END`
        `CLASS_LINE_START`
        `CLASS_LINE_END`
        `CLASS_EMPTY_LINE`
        """
        ...

    def find_by_class(self, pt: Point, forward: bool, classes: int, separators: str = "") -> Region:
        """
        Finds the next location after point that matches the given classes
        If forward is `False`, searches backwards instead of forwards.
        classes is a bitwise OR of the `CLASS_XXX` flags
        `separators` may be passed in, to define what characters should be
        considered to separate words
        """
        ...

    def expand_by_class(
        self, x: Union[Region, Point], classes: int, separators: str = ""
    ) -> Region:
        """
        Expands `x` to the left and right, until each side lands on a location
        that matches `classes`. classes is a bitwise OR of the
        `CLASS_XXX` flags. `separators` may be passed in, to define
        what characters should be considered to separate words
        """
        ...

    def rowcol(self, tp: Point) -> Tuple[int, int]:
        """ Calculates the 0-based line and column numbers of the the given point """
        ...

    def rowcol_utf8(self, tp: Point) -> Tuple[int, int]:
        """ (UTF-8) Calculates the 0-based line and column numbers of the the given point """
        ...

    def rowcol_utf16(self, tp: Point) -> Tuple[int, int]:
        """ (UTF-16) Calculates the 0-based line and column numbers of the the given point """
        ...

    def text_point(self, row: int, col: int, *, clamp_column: bool = False) -> int:
        """
        Converts a row and column into a text point

        clamp_column: A bool, if col should be restricted to valid values for the given row
        """
        ...

    def text_point_utf8(self, row: int, col: int, *, clamp_column: bool = False) -> int:
        """
        (UTF-8) Converts a row and column into a text point

        clamp_column: A bool, if col should be restricted to valid values for the given row
        """
        ...

    def text_point_utf16(self, row: int, col: int, *, clamp_column: bool = False) -> int:
        """
        (UTF-16) Converts a row and column into a text point

        clamp_column: A bool, if col should be restricted to valid values for the given row
        """
        ...

    def visible_region(self) -> Region:
        """ Returns the approximate visible region """
        ...

    def show(
        self,
        x: Union[Selection, Region, Point],
        show_surrounds: bool = True,
        keep_to_left: bool = False,
        animate: bool = True,
    ) -> None:
        """ Scrolls the view to reveal x, which may be a Region or point """
        ...

    def show_at_center(self, x: Union[Region, Point]) -> None:
        """ Scrolls the view to center on x, which may be a Region or point """
        ...

    def viewport_position(self) -> Vector:
        """ Returns the (x, y) scroll position of the view in layout coordinates """
        ...

    def set_viewport_position(self, xy: Vector, animate: bool = True) -> None:
        """ Scrolls the view to the given position in layout coordinates """
        ...

    def viewport_extent(self) -> Vector:
        """ Returns the width and height of the viewport, in layout coordinates """
        ...

    def layout_extent(self) -> Vector:
        """ Returns the total height and width of the document, in layout coordinates """
        ...

    def text_to_layout(self, tp: Point) -> Vector:
        """ Converts a text point to layout coordinates """
        ...

    def text_to_window(self, tp: Point) -> Vector:
        """ Converts a text point to window coordinates """
        ...

    def layout_to_text(self, xy: Vector) -> int:
        """ Converts layout coordinates to a text point """
        ...

    def layout_to_window(self, xy: Vector) -> Vector:
        """ Converts layout coordinates to window coordinates """
        ...

    def window_to_layout(self, xy: Vector) -> Vector:
        """ Converts window coordinates to layout coordinates """
        ...

    def window_to_text(self, xy: Vector) -> int:
        """ Converts window coordinates to a text point """
        ...

    def line_height(self) -> float:
        """ Returns the height of a line in layout coordinates """
        ...

    def em_width(self) -> float:
        """ Returns the em-width of the current font in layout coordinates """
        ...

    def is_folded(self, sr: Region) -> bool:
        """ Determines whether the given region is folded """
        ...

    def folded_regions(self) -> List[Region]:
        """ Gets folded regions in the view """
        ...

    def fold(self, x: Union[Region, List[Region]]) -> bool:
        """ Folds the given regions, returning False if they were already folded """
        ...

    def unfold(self, x: Union[Region, List[Region]]) -> List[Region]:
        """ Unfolds all text in the region, returning the unfolded regions """
        ...

    def add_regions(
        self,
        key: str,
        regions: List[Region],
        scope: str = "",
        icon: str = "",
        flags: int = 0,
        annotations: List[str] = [],
        annotation_color: str = "",
        on_navigate: Optional[Callback1[str]] = None,
        on_close: Optional[Callback0] = None,
    ) -> None:
        """
        Add a set of `regions` to the view. If a set of regions already exists
        with the given `key`, they will be overwritten. The `scope` is used
        to source a color to draw the regions in, it should be the name of a
        scope, such as "comment" or "string". If the scope is empty, the
        regions won't be drawn.

        The optional `icon` name, if given, will draw the named icons in the
        gutter next to each region. The `icon` will be tinted using the color
        associated with the `scope`. Valid icon names are dot, circle and
        bookmark. The `icon` name may also be a full package relative path
        such as _Packages/Theme - Default/dot.png_.

        The optional `flags` parameter is a bitwise combination of:

        `DRAW_EMPTY`: Draw empty regions with a vertical bar
        By default, they aren't drawn at all.

        `HIDE_ON_MINIMAP`: Don't show the regions on the minimap.

        `DRAW_EMPTY_AS_OVERWRITE`: Draw empty regions with a horizontal
        bar instead of a vertical one.

        `DRAW_NO_FILL`: Disable filling the regions, leaving only the outline.

        `DRAW_NO_OUTLINE`: Disable drawing the outline of the regions.

        `DRAW_SOLID_UNDERLINE`: Draw a solid underline below the regions.

        `DRAW_STIPPLED_UNDERLINE`: Draw a stippled underline below the regions.

        `DRAW_SQUIGGLY_UNDERLINE`: Draw a squiggly underline below the regions.

        `PERSISTENT`: Save the regions in the session.

        `HIDDEN`: Don't draw the regions.

        The underline styles are exclusive, either zero or one of them should
        be given. If using an underline, `DRAW_NO_FILL` and
        `DRAW_NO_OUTLINE` should generally be passed in
        """
        ...

    def get_regions(self, key: str) -> List[Region]:
        """ Return the regions associated with the given `key`, if any """
        ...

    def erase_regions(self, key: str) -> None:
        """ Remove the named regions """
        ...

    def add_phantom(
        self,
        key: str,
        region: Region,
        content: str,
        layout: int,
        on_navigate: Optional[Callback1[str]] = None,
    ) -> int:
        ...

    def erase_phantoms(self, key: str) -> None:
        """ Remove the named phantoms """
        ...

    def erase_phantom_by_id(self, pid: int) -> None:
        """ Remove the phantom with the given phantom ID """
        ...

    def query_phantom(self, pid: int) -> List[Tuple[int, int]]:
        ...

    def query_phantoms(self, pids: List[int]) -> List[Tuple[int, int]]:
        ...

    def assign_syntax(self, syntax_file: str) -> None:
        """
        Sets the syntax for this view.

        You can use "Packages/Python/Python.sublime-syntax" or "scope:source.python"
        """
        ...

    def set_syntax_file(self, syntax_file: str) -> None:
        """ Deprecated, use `assign_syntax()` instead """
        ...

    def symbols(self) -> List[Tuple[Region, str]]:
        """ Extract all the symbols defined in the buffer """
        ...

    def get_symbols(self) -> List[Tuple[Region, str]]:
        """ Deprecated, use `symbols()` instead """
        ...

    def indexed_symbols(self) -> List[Tuple[Region, str]]:
        ...

    def indexed_references(self) -> List[Tuple[Region, str]]:
        ...

    def set_status(self, key: str, value: str) -> None:
        """
        Adds the status `key` to the view. The value will be displayed in the
        status bar, in a comma separated list of all status values, ordered by key
        Setting the value to the empty string will clear the status
        """
        ...

    def get_status(self, key: str) -> str:
        """ Returns the previously assigned value associated with the `key`, if any """
        ...

    def erase_status(self, key: str) -> None:
        """ Clears the named status """
        ...

    def extract_completions(self, prefix: str, tp: Point = -1) -> List[str]:
        ...

    def find_all_results(self) -> List[Tuple[str, int, int]]:
        ...

    def find_all_results_with_text(self) -> List[Tuple[str, int, int, str]]:
        ...

    def command_history(
        self, delta: int, modifying_only: bool = False
    ) -> Tuple[Optional[str], Optional[Dict[str, Any]], int]:
        """
        Returns the command name, command arguments, and repeat count for the
        given history entry, as stored in the undo / redo stack.

        Index 0 corresponds to the most recent command, -1 the command before
        that, and so on. Positive values for `delta` indicates to look in the
        redo stack for commands. If the undo / redo history doesn't extend far
        enough, then `(None, None, 0)` will be returned.

        Setting `modifying_only` to `True` will only return entries that
        modified the buffer
        """
        ...

    def overwrite_status(self) -> bool:
        """ Returns the overwrite status, which the user normally toggles via the insert key """
        ...

    def set_overwrite_status(self, value: bool) -> None:
        """ Sets the overwrite status """
        ...

    def show_popup_menu(
        self, items: Sequence[str], on_select: Callback1[int], flags: int = 0
    ) -> None:
        """
        Shows a pop up menu at the caret, to select an item in a list. `on_done`
        will be called once, with the index of the selected item. If the pop up
        menu was cancelled, `on_done` will be called with an argument of -1.

        `items` is a list of strings.

        `flags` is currently unused
        """
        ...

    def show_popup(
        self,
        content: str,
        flags: int = 0,
        location: int = -1,
        max_width: int = 320,
        max_height: int = 240,
        on_navigate: Optional[Callback1[str]] = None,
        on_hide: Optional[Callback0] = None,
    ) -> None:
        """
        Shows a popup displaying HTML content.

        * `flags` is a bitwise combination of the following:

        `COOPERATE_WITH_AUTO_COMPLETE`: Causes the popup to display next to the auto complete menu
        `HIDE_ON_MOUSE_MOVE`: Causes the popup to hide when the mouse is moved, clicked or scrolled
        `HIDE_ON_MOUSE_MOVE_AWAY`: Causes the popup to hide when the mouse is moved
                                    (unless towards the popup), or when clicked or scrolled
        * `location` sets the location of the popup, if -1 (default) will display
        the popup at the cursor, otherwise a text point should be passed.

        * `max_width` and `max_height` set the maximum dimensions for the popup,
        after which scroll bars will be displayed.

        * `on_navigate` is a callback that should accept a string contents of the
        href attribute on the link the user clicked.

        * `on_hide` is called when the popup is hidden
        """
        ...

    def update_popup(self, content: str) -> None:
        """ Updates the contents of the currently visible popup """
        ...

    def is_popup_visible(self) -> bool:
        """ Returns if the popup is currently shown """
        ...

    def hide_popup(self) -> None:
        """ Hides the popup """
        ...

    def is_auto_complete_visible(self) -> bool:
        """ Returns wether the auto complete menu is currently visible """
        ...

    def preserve_auto_complete_on_focus_lost(self) -> None:
        """ Make the auto complete menu when this view loses focus """
        ...


class Settings:

    settings_id: int

    def __init__(self, id: int) -> None:
        ...

    def __getitem__(self, key: str) -> Value:
        ...

    def __setitem__(self, key: str, value: Value) -> None:
        ...

    def __delitem__(self, key: str) -> None:
        ...

    def __contains__(self, key: str) -> bool:
        ...

    def __repr__(self) -> str:
        ...

    def to_dict(self) -> Dict[str, Value]:
        """
        Return the settings as a dict. This is not very fast.

        Warning: Python 3.8 only.
        """
        ...

    def setdefault(self, key: str, value: Value) -> Value:
        """
        Returns the value of the item with the specified key.

        If the key does not exist, insert the key, with the specified value, see example below.
        """
        ...

    def update(self, other: Union[Dict, Iterable] = (), /, **kwargs) -> None:
        """
        Inserts the specified items to this Settings.

        The specified items can be a dictionary, or an iterable object.
        """
        ...

    def get(self, key: str, default: Optional[Value] = None) -> Value:
        """
        Returns the named setting, or `default` if it's not defined
        If not passed, `default` will have a value of `None`
        """
        ...

    def has(self, key: str) -> bool:
        """
        Returns `True` if the named option exists in this set of Settings or
        one of its parents
        """
        ...

    def set(self, key: str, value: Value) -> None:
        """ Sets the named setting. Only primitive types, lists, and dicts are accepted """
        ...

    def erase(self, key: str) -> None:
        """ Removes the named setting. Does not remove it from any parent Settings """
        ...

    def add_on_change(self, tag: str, callback: Callback0) -> None:
        """ Register a `callback` to be run whenever a setting in this object is changed """
        ...

    def clear_on_change(self, tag: str) -> None:
        """ Remove all callbacks registered with the given `tag` """
        ...


class Phantom:
    """
    Creates a phantom attached to a region

    * `content` is HTML to be processed by _minihtml_.

    * `layout` must be one of:

    - `LAYOUT_INLINE`: Display the phantom in between the region and the point following.
    - `LAYOUT_BELOW`: Display the phantom in space below the current line,
                    left-aligned with the region.
    - `LAYOUT_BLOCK`: Display the phantom in space below the current line,
    left-aligned with the beginning of the line.

    * `on_navigate` is an optional callback that should accept a single string
    parameter, that is the _href_ attribute of the link clicked.
    """

    region: Region
    content: str
    layout: int
    on_navigate: Optional[Callback1[str]]
    id: int

    def __init__(
        self,
        region: Region,
        content: str,
        layout: int,
        on_navigate: Optional[Callback1[str]] = None,
    ) -> None:
        ...

    def __eq__(self, rhs: "Phantom") -> bool:
        ...

    def __repr__(self) -> str:
        ...

    def to_tuple(self) -> Tuple[Tuple[int, int], str, Layout, Optional[Callback1[str]]]:
        """
        Returns a tuple of this phantom.

        Use this to uniquely identify a phantom in a set or similar. Phantoms
        can't be used for that directly as they may be mutated.

        The phantom's range will also be returned as a tuple.
        """
        ...


class PhantomSet:
    """
    A collection that manages Phantoms and the process of adding them,
    updating them and removing them from the View
    """

    view: View
    key: str
    phantoms: List[Phantom]

    def __init__(self, view: View, key: str = "") -> None:
        ...

    def __del__(self) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def update(self, new_phantoms: Sequence[Phantom]) -> None:
        """
        phantoms should be a list of phantoms.

        The `region` attribute of each existing phantom in the set will be updated.
        New phantoms will be added to the view and phantoms not in phantoms list will be deleted.
        """
        ...


class Html:
    data: Any

    def __init__(self, data: Any) -> None:
        ...

    def __repr__(self) -> str:
        ...


class CompletionList:
    """
    Represents a list of completions,
    some of which may be in the process of being asynchronously fetched
    """

    target: Optional[Any]
    completions: List[T_completion]
    flags: int

    def __init__(self, completions: List[T_completion] = None, flags: int = 0) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def _set_target(self, target: Optional[Any]) -> None:
        ...

    def set_completions(self, completions: List[T_completion], flags: int = 0):
        """ Sets the completions """
        ...


class CompletionItem:
    """ Represents an available auto-completion item """

    trigger: str
    annotation: str
    completion: T_completion
    completion_format: int
    kind: Tuple[int, str, str]
    details: str
    flags: int

    def __init__(
        self,
        trigger: str,
        annotation: str = "",
        completion: T_completion = "",
        completion_format: int = COMPLETION_FORMAT_TEXT,
        kind: Tuple[int, str, str] = KIND_AMBIGUOUS,
        details: str = "",
    ) -> None:
        ...

    def __eq__(self, rhs: "CompletionItem") -> bool:
        ...

    def __repr__(self) -> str:
        ...

    @classmethod
    def snippet_completion(
        cls,
        trigger: str,
        snippet: str,
        annotation: str = "",
        kind: Tuple[int, str, str] = KIND_SNIPPET,
        details: str = "",
    ) -> "CompletionItem":
        """
        trigger: A unicode string of the text to match against the user's input.

        snippet: The snippet text to insert if the item is selected.

        annotation: An optional unicode string of a hint to draw to
        the right-hand side of the trigger.

        kind: An optional completion_kind tuple that controls the presentation
        in the auto-complete window – defaults to sublime.KIND_SNIPPET.

        details: An optional HTML description of the completion,
        shown in the detail pane at the bottom of the auto complete window.
        Only supports limited inline HTML, including the tags:
        `<a href="">` `<b>` `<strong>` `<i>` `<em>` `<u>` `<tt>` `<code>`
        """
        ...

    @classmethod
    def command_completion(
        cls,
        trigger: str,
        command: str,
        args: Dict[str, Value] = {},
        annotation: str = "",
        kind: Tuple[int, str, str] = KIND_AMBIGUOUS,
        details: str = "",
    ) -> "CompletionItem":
        """
        trigger: A unicode string of the text to match against the user's input.

        command: A unicode string of the command to execute

        args: An optional dict of args to pass to the command

        annotation: An optional unicode string of a hint to draw to
        the right-hand side of the trigger.

        kind: An optional completion_kind tuple that controls the presentation
        in the auto-complete window – defaults to sublime.KIND_AMBIGUOUS.

        details: An optional HTML description of the completion,
        shown in the detail pane at the bottom of the auto complete window.
        Only supports limited inline HTML, including the tags:
        `<a href="">` `<b>` `<strong>` `<i>` `<em>` `<u>` `<tt>` `<code>`
        """
        ...
