# Complete decomposition process

Current decomposition process (Check `./adabox/complete`):
1. [binary_matrix_to_rec_list.py](1_binary_matrix_to_rec_list.py)
2. [rec_list_to_group_intf_details.py](2_rec_list_to_group_intf_details.py)
3. [group_intf_details_to_gexf_partitioned.py](3_group_intf_details_to_gexf_partitioned.py)
4. [gexf_partitioned_to_gpu_device_global_data.py](4_gexf_partitioned_to_gpu_device_global_data.py)

Install METIS:
- https://formulae.brew.sh/formula/metis
- setting up environment variable. For instance add **"METIS_DLL=/opt/homebrew/Cellar/metis/5.1.0/lib/libmetis.dylib"** to `~/.zshrc`
