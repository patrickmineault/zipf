import argparse
import pandas as pd
import pathlib

from zipf.parse_text import count_words
from zipf.fit_distribution import compute_summary


def main(args):
    # Process all text files.
    paths = list(pathlib.Path(args.in_folder).glob("*.txt"))

    if not paths:
        raise Exception(f"No text files found in {args.in_folder}")

    # Create the paths if necessary
    out_path = pathlib.Path(args.out_folder)
    out_path.mkdir(exist_ok=True)
    (out_path / "raw_counts").mkdir(exist_ok=True)

    summaries = []
    for p in paths:
        print(p)
        with open(p, "r") as f:
            word_counts = count_words(f, True)

        df = pd.DataFrame(
            [
                {"word": x, "freq": y}
                for x, y in zip(word_counts.keys(), word_counts.values())
            ]
        )
        df = df.sort_values("freq", ascending=False)
        out_file = out_path / "raw_counts" / (p.stem + ".csv")
        df.to_csv(out_file)

        summary = compute_summary(word_counts)
        summary["name"] = p.stem
        summaries.append(summary)

    pd.DataFrame(summaries).to_csv(pathlib.Path(args.out_folder) / "summary.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute zipf distribution")
    parser.add_argument("--in_folder", help="the input folder")
    parser.add_argument("--out_folder", help="the output folder")
    args = parser.parse_args()

    main(args)
