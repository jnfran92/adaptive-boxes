# CHANGELOG

## 19 Feb 2023
Summary of the decomposition process:
- Decompose binary matrix into list of rectangles: [sample9.py](adabox%2Fdecomposition%2Fsamples%2Fsample9.py)
- List of Rectangles to group/interface details(summary_groups, x_units, y_units, group_details): [post_process_csv_gpu.py](legacy%2Fpostproc_gpu%2Fpost_process_csv_gpu.py)
- Group/interface details to 
- proto_2.py changed to [create_partitions_with_metis.py](graph%2Fproto%2Fmetis%2Fcreate_partitions_with_metis.py)


## 7 Feb 2023
- Check sample 9 to generate adabox partitions, this implementation is not set in a new file yet.
- [getters_completed.so](adabox%2Fdecomposition%2Fcpp%2Fgetters_completed.so) is required to run adabox, more info check Readme inside.
- [partitions_data](graph%2Fpartitions_data) check scripts for partition analysis using metis.
- Check this file to post proc partitions with adabox: [post_process_csv_gpu.py](legacy%2Fpostproc_gpu%2Fpost_process_csv_gpu.py)
- Last proto file for Metis: [proto_2.py](graph%2Fproto%2Fmetis%2Fproto_2.py)


