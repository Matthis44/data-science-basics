from hackerrank import (
    Queue,
    TextEditor,
    cookies,
    is_balanced,
    lego_blocks,
    pairs,
    super_digit,
)


def test_pairs():
    assert pairs(2, [1, 5, 3, 4, 2]) == 3


def test_queue_with_two_stacks():
    q = Queue()
    q.enqueue(42)
    q.enqueue(14)
    assert q.front() == 42
    assert q.dequeue() == 42
    q.enqueue(28)
    assert q.front() == 14
    assert [q.dequeue(), q.dequeue(), q.dequeue()] == [14, 28, None]


def test_balanced_brackets():
    assert is_balanced("{[()]}") == "YES"
    assert is_balanced("{[(])}") == "NO"
    assert is_balanced("{{[[(())]]}}") == "YES"
    assert is_balanced("((") == "NO"


def test_super_digit():
    assert super_digit("148", 3) == 3
    assert super_digit("9875", 4) == 8


def test_cookies():
    assert cookies(7, [1, 2, 3, 9, 10, 12]) == 2
    assert cookies(100, [1, 1]) == -1


def test_lego_blocks():
    assert lego_blocks(2, 2) == 3
    assert lego_blocks(3, 2) == 7
    assert lego_blocks(2, 3) == 9
    assert lego_blocks(4, 4) == 3375


def test_text_editor():
    editor = TextEditor()
    editor.append("abc")
    assert editor.char_at(3) == "c"
    editor.delete(3)
    editor.append("xy")
    assert editor.char_at(2) == "y"
    editor.undo()
    editor.undo()
    assert editor.char_at(1) == "a"
