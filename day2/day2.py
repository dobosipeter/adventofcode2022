from enum import Enum


def day2(input_path: str) -> None:
    """
    Calculate the score of the game.
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
            case FirstMoves.PAPER:
                # Check the second players move
                match second_move:
                    case SecondMoves.ROCK:
                        pass
                    case SecondMoves.PAPER:
                        pass
                    case SecondMoves.SCISSORS:
                        pass
            case FirstMoves.SCISSORS:
                # Check the second players move
                match second_move:
                    case SecondMoves.ROCK:
                        pass
                    case SecondMoves.PAPER:
                        pass
                    case SecondMoves.SCISSORS:
                        pass


