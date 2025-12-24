# Standard Libraries
import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    
    # Token related arguments
    parser.add_argument('-ts', '--tokenservice', help='The service name related to the token.', required=True)
    parser.add_argument('-tn', '--tokenname', help='The name of the token stored.', required=True)

    # Database related arguments
    parser.add_argument('-db', '--database', help='The path to the SQLite database.', required=True)

    # Logging related arguments
    parser.add_argument('-ld', '--loggingdestination', help='The path where you would like to dump logs.', required=True)
    parser.add_argument('-ll', '--logginglevel', help='The level of logging desired.', required=True)

    # Testing related arguments
    parser.add_argument('-tg', '--testguild', type=int, help='The discord guild id for the test server.', required=True)

    args = parser.parse_args()
    return args
    

