import argparse
from enum import Enum

from app.live.live import LiveAnalysisApp
from app.video.video import VideoAnalysisApp


class AppTypes(Enum):
    LIVE = LiveAnalysisApp
    VIDEO = VideoAnalysisApp


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Visualization parameters")

    required = parser.add_argument_group("Required arguments")
    required.add_argument(
        "-a",
        "--app",
        choices=["LIVE", "VIDEO"],
        help="Application type (Live, Video)",
        required=True,
    )
    required.add_argument(
        "-i",
        "--input",
        help="Camera numer or path to video",
        type=lambda x: int(x) if x.isdigit() else x,
        required=True,
    )
    required.add_argument(
        "--exercise",
        help="Type of exercise",
        type=str,
        required=True,
    )

    optional = parser.add_argument_group("Optional arguments")
    optional.add_argument(
        "-o", "--output", help="Output path for joints results", default="results"
    )
    optional.add_argument(
        "--save_results",
        help="If positions should be saved or not",
        action="store_true",
    )
    optional.add_argument(
        "--loop",
        help="If video should be looped or not",
        action="store_true",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    try:
        app_type = AppTypes[args.app]
        app = app_type.value()
    except KeyError:
        raise ValueError("Invalid app type")
    app.run(args)


if __name__ == "__main__":
    main()