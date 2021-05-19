""" Contains utilities related to io """
import os
import yaml


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


def write_all_data_to_file(file_path, data, mode="w", create_parent_dirs=False):
    if create_parent_dirs:
        _make_par_dirs(os.path.dirname(file_path))
    with open(file_path, mode=mode) as out_stream:
        out_stream.write(data)


def get_abs_path(rel_path, caller_script_directory):
    return os.path.join(os.path.dirname(caller_script_directory), rel_path)