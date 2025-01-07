from dag_datalake_sirene.config import (
    MINIO_BASE_URL,
    DATA_GOUV_BASE_URL,
    DataSourceConfig,
)

BILANS_FINANCIERS_CONFIG = DataSourceConfig(
    name="bilans_financiers",
    tmp_folder=f"{DataSourceConfig.base_tmp_folder}/bilans_financiers",
    minio_path="bilans_financiers",
    file_name="synthese_bilans",
    files_to_download={
        "bilans_financiers": {
            "url": f"{DATA_GOUV_BASE_URL}9d213815-1649-4527-9eb4-427146ef2e5b",
            "resource_id": "9d213815-1649-4527-9eb4-427146ef2e5b",
            "destination": f"{DataSourceConfig.base_tmp_folder}/bilans_financiers/bilans-financiers-download.csv",
        }
    },
    url_minio=f"{MINIO_BASE_URL}bilans_financiers/latest/synthese_bilans.csv",
    url_minio_metadata=f"{MINIO_BASE_URL}bilans_financiers/latest/metadata.json",
    file_output=f"{DataSourceConfig.base_tmp_folder}/bilans_financiers/synthese_bilans.csv",
)
