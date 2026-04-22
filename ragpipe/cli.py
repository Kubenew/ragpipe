import argparse
import json

from .loaders import load_directory
from .pipeline import ingest_file, ingest_url


def main():
    parser = argparse.ArgumentParser(prog="ragpipe", description="RAG ingestion pipeline CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_ingest = sub.add_parser("ingest", help="Ingest directory of .txt/.md")
    p_ingest.add_argument("path")
    p_ingest.add_argument("--out", required=True)

    p_url = sub.add_parser("ingest-url", help="Ingest a URL")
    p_url.add_argument("url")
    p_url.add_argument("--out", required=True)

    args = parser.parse_args()

    if args.cmd == "ingest":
        docs = load_directory(args.path)
        out_data = {"documents": []}
        for fp in docs:
            out_data["documents"].append(ingest_file(fp))
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(out_data, f, indent=2, ensure_ascii=False)
        print(f"Wrote {args.out}")
    else:
        data = ingest_url(args.url)
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
