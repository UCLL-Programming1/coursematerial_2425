import time
time.sleep(10)
import pytest
import student


def join(lines):
    return "".join(f'{line}\n' for line in lines)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("contents, expected", [
    *(
        (join(lines), join(line for line in lines if line))
        for lines in [
            [
                ''
            ],
            [
                ' '
            ],
            [
                'a'
            ],
            [
                'a',
                '',
            ],
            [
                'a',
                '',
                '',
                '',
            ],
            [
                'a',
                'b',
            ],
            [
                'a',
                '',
                'b',
            ],
            [
                'a',
                '   ',
                'b',
            ],
            [
                '',
                'line',
                '',
                '',
                '',
                'line',
                '',
                'line',
                '',
                'line',
                '',
                'line',
                '',
            ]
        ]
    )
])
@pytest.mark.parametrize('source', [
    'a.txt',
    'input.txt',
])
@pytest.mark.parametrize('destination', [
    'b.txt',
    'output.txt',
])
def test_remove_empty_lines(tmp_path, source, destination, contents, expected):
    source_path = tmp_path / source
    destination_path = tmp_path / destination
    source_path.write_text(contents)

    student.remove_empty_lines(str(source_path), str(destination_path))

    assert destination_path.is_file()
    assert expected == destination_path.read_text()
