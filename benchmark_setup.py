# Copyright (C) 2022 Maxim Lippeveld
#
# This file is part of SCIP.
#
# SCIP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SCIP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SCIP.  If not, see <http://www.gnu.org/licenses/>.

from pathlib import Path
from datetime import datetime
import uuid
import pandas
import os


def main(a):

    vo = Path(os.environ["VSC_DATA_VO_USER"])
    output = vo / "results/scip_benchmark"
    output = output / Path("benchmark_%s" % datetime.now().strftime("%Y%m%d%H%M%S"))
    output.mkdir(parents=True)
    (output / "results").mkdir()

    iterations = 10
    commands = []

    if a == "size":
        total_mem = 96
        n_workers = 16

        for limit in [100, 1_000, 10_000, 100_000, 1_000_000]:
            for partition_size in [100, 200, 400, 800, 1600]:
                for _ in range(iterations):
                    ident = uuid.uuid4()

                    o = str(output / "results" / str(ident))

                    commands.append(dict(
                        n_workers=n_workers,
                        memory=total_mem // n_workers,
                        partition_size=partition_size,
                        output=o,
                        np=n_workers + 2,
                        prefix=str(output),
                        data= (vo / "datasets/benchmark_datasets") / f"{str(limit)}.zarr"
                    ))

    if a == "n_workers":
        total_mem = 96
        # partition_size = 200

        for n_workers in [1, 2, 4, 8, 16, 32]:
            for partition_size in [100, 400, 800, 1600]:
                for _ in range(iterations):
                    ident = uuid.uuid4()

                    o = str(output / "results" / str(ident))

                    commands.append(dict(
                        n_workers=n_workers,
                        memory=total_mem // n_workers,
                        partition_size=partition_size,
                        output=o,
                        np=n_workers + 2,
                        prefix=str(output)
                    ))

    pandas.DataFrame(commands).to_csv(str(output / "data.csv"), index=False)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", type=str)

    args = parser.parse_args()
    main(args.a)
