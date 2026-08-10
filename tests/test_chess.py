import os

import pytest

TESTS_DIR = os.path.join(os.path.dirname(__file__))


@pytest.mark.rotation
@pytest.mark.pawn
def test_no_moves(run_chess_case):
    run_chess_case(os.path.join(TESTS_DIR, "001-no-moves.test"))


@pytest.mark.pawn
def test_simple_error(run_chess_case):
    run_chess_case(os.path.join(TESTS_DIR, "011-simple-error.test"))


@pytest.mark.rotation
@pytest.mark.pawn
def test_simple(run_chess_case):
    run_chess_case(os.path.join(TESTS_DIR, "012-simple-move.test"))


@pytest.mark.rotation
def test_color_rotation_error(run_chess_case):
    run_chess_case(os.path.join(TESTS_DIR, "013-color-rotation-error.test"))


@pytest.mark.rotation
@pytest.mark.pawn
def test_color_rotation_correct(run_chess_case):
    run_chess_case(os.path.join(TESTS_DIR, "014-color-rotation-correct.test"))


@pytest.mark.rotation
@pytest.mark.pawn
def test_pawn_moves_one_square_vertically(run_chess_case):
    run_chess_case(os.path.join(TESTS_DIR, "021-pawn-moves-one-square-vertically.test"))


@pytest.mark.rotation
@pytest.mark.pawn
def test_pawn_can_move_two_squares_on_first_move(run_chess_case):
    run_chess_case(os.path.join(TESTS_DIR, "022-pawn-can-move-two-squares-on-first-move.test"))


@pytest.mark.pawn
def test_pawn_can_not_move_diagonally(run_chess_case):
    run_chess_case(os.path.join(TESTS_DIR, "023-pawn-can-not-move-diagonally.test"))


@pytest.mark.rotation
@pytest.mark.pawn
def test_pawn_captures_diagonally(run_chess_case):
    run_chess_case(os.path.join(TESTS_DIR, "024-pawn-captures-diagonally.test"))


@pytest.mark.pawn
def test_pawn_can_not_capture_vertically(run_chess_case):
    run_chess_case(os.path.join(TESTS_DIR, "025-pawn-can-not-capture-vertically.test"))


@pytest.mark.pawn
def test_pawn_can_not_move_farther_one_square(run_chess_case):
    run_chess_case(os.path.join(TESTS_DIR, "026-pawn-can-not-move-farther-one-square.test"))


@pytest.mark.pawn
def test_pawn_can_not_move_across_figure(run_chess_case):
    run_chess_case(os.path.join(TESTS_DIR, "027-pawn-can-not-move-across-figure.test"))
