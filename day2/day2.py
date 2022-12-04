from enum import Enum


def solve(input_path: str) -> None:
    """
    Calculate the total score of the games.
    :param input_path: The path of the input file, containing the moves made by the players
    :return: Nothing, prints the final score.
    """
    class FirstMoves(Enum):
        """
        An enum representing the encoding of the moves in the first column.
        """
        ROCK = "A"
        PAPER = "B"
        SCISSORS = "C"

    class SecondMoves(Enum):
        """
        An enum representing the encoding of the scores in the second column.
        """
        ROCK = "X"
        PAPER = "Y"
        SCISSORS = "Z"

    class MoveScores(Enum):
        """
        An enum representing the points awarded for making each move.
        """
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    class OutcomeScores(Enum):
        """
        An enum representing the points awarded for each possible match outcome.
        """
        LOST = 0
        DRAW = 3
        WIN = 6

    def determine_score(first_move: FirstMoves, second_move: SecondMoves) -> int:
        """
        Given two moves, determines the score of the second player.

        :param first_move: The move made by the first player.
        :param second_move: The move made by the second player.

        :return: The combined score of the second player for playing the match.
        """
        # Determine the winner
        # Check the first players move
        match first_move:
            case FirstMoves.ROCK:
                # Check the second players move
                match second_move:
                    case SecondMoves.ROCK:
                        return MoveScores.ROCK.value + OutcomeScores.DRAW.value
                    case SecondMoves.PAPER:
                        return MoveScores.PAPER.value + OutcomeScores.WIN.value
                    case SecondMoves.SCISSORS:
                        return MoveScores.SCISSORS.value + OutcomeScores.LOST.value
            # Check the first players move
            case FirstMoves.PAPER:
                # Check the second players move
                match second_move:
                    case SecondMoves.ROCK:
                        return MoveScores.ROCK.value + OutcomeScores.LOST.value
                    case SecondMoves.PAPER:
                        return MoveScores.PAPER.value + OutcomeScores.DRAW.value
                    case SecondMoves.SCISSORS:
                        return MoveScores.SCISSORS.value + OutcomeScores.WIN.value
            case FirstMoves.SCISSORS:
                # Check the second players move
                match second_move:
                    case SecondMoves.ROCK:
                        return MoveScores.ROCK.value + OutcomeScores.WIN.value
                    case SecondMoves.PAPER:
                        return MoveScores.PAPER.value + OutcomeScores.LOST.value
                    case SecondMoves.SCISSORS:
                        return MoveScores.SCISSORS.value + OutcomeScores.DRAW.value

    def read_input(file_path: str) -> list:
        """
        Reads the input from the file.

        :param file_path: The path of the file containing the moves to read.
        :return: The moves in a nested list.
        """
        moves = []
        # Read the lines
        file = open(file_path)
        lines = file.read().splitlines()
        # Convert them into a format that we can handle
        for line in lines:
            moves.append(line.split(" "))
        return moves

    def convert_moves(moves: list) -> list:
        """
        Convert moves from strings to the move enums format.

        :param moves: The move strings to convert.
        :return: The converted moves.
        """
        # Iterate through the moves
        for move_pairs in moves:
            for move in move_pairs:
                pass

    # Do the actual calculation
    moves_as_strings = read_input(input_path)
    print(moves_as_strings)
