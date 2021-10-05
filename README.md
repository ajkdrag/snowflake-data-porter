# Snowflake-Data-Porter
Utility for moving data from local to snowflake tables and vice versa

## Usage
Clone/Download this repo.
```bash
git clone https://github.com/ajkdrag/Snowflake-Data-Porter
```

Go to the root dir and add it to **PYTHONPATH** 
```bash
cd Snowflake-Data-Porter
export PYTHONPATH=$(pwd)
```

Place your Snowflake creds in *snowflake_conn.cfg.yaml* and configurations in *data_porter.cfg.yaml*
```bash
src/
├── configs
│   ├── data_porter.cfg.yaml
│   ├── globals.cfg.yaml
│   └── snowflake_conn.cfg.yaml
```

Create a temporary working dir and run the launcher script.
```bash
mkdir src/tmp
python src/launcher.py --config src/configs/data_porter.cfg.yaml --wrk-dir tmp
```

This runs all the [supported operations](#supported-operations) defined in *data_porter.cfg.yaml*  

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[Standard GPL 3.0](https://choosealicense.com/licenses/gpl-3.0/)


