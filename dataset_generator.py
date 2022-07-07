import zarr
from pathlib import Path
import numcodecs
import numpy

sizes = [100, 1_000, 10_000, 100_000, 1_000_000]
orig = zarr.open("")

z = zarr.open(
    str(Path("/kyukon/home/gent/420/vsc42015/vsc_data_vo/" +
        "datasets/wbc/images/sample0/sample0_part1_of_3.zarr")),
    mode="r"
)
output_root = Path("/kyukon/home/gent/420/vsc42015/vsc_data_vo/datasets/benchmark_datasets")

for size in sizes:
    print(size)
    output = output_root / f"{str(size)}.zarr"
    store = zarr.storage.DirectoryStore(output)
    o = zarr.open(
        store=store,
        shape=(size,),
        mode="w",
        chunks=(1000,),
        dtype=object,
        object_codec=numcodecs.VLenArray('u2')
    )
    o.attrs["object_number"] = numpy.resize(z.attrs["object_number"], (size,)).tolist()
    o.attrs["shape"] = numpy.resize(z.attrs["shape"], (size,3)).tolist()

    if len(z) > size:
        o[:] = z[:size]
    else:
        o[:] = numpy.resize(z, (size,))
