""" Contains utilities related to io """
import os
import yaml
import pandas as pd


def get_all_data_from_yaml(yaml_file_path):
    with open(yaml_file_path) as in_stream:
        content = yaml.safe_load(in_stream) or {}
        return content


def get_all_data_from_file(file_path):
    with open(file_path) as in_stream:
        return in_stream.read()


def _make_par_dirs(path):
    os.makedirs(path, exist_ok=True)


def join(*args):
    return os.path.join(*args)


def get_dataframe_from_list(list_of_dicts):
    return pd.DataFrame(list_of_dicts)


def write_all_data_to_file(file_path, data, mode="w", create_parent_dirs=False):
    if create_parent_dirs:
        _make_par_dirs(os.path.dirname(file_path))
    with open(file_path, mode=mode) as out_stream:
        out_stream.write(data)


def write_dataframe_to_file(
    file_path, dataframe, mode="w", create_parent_dirs=False, index=False
):
    if create_parent_dirs:
        _make_par_dirs(os.path.dirname(file_path))
    dataframe.to_csv(file_path, mode=mode, index=index)


def get_abs_path(rel_path, caller_script_directory):
    return os.path.join(os.path.dirname(caller_script_directory), rel_path)
