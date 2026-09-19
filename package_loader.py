from DB_Side import DBLoader
from module.CSVModule import csv_import

def export_table(table_name: str, attributes: tuple, indata: list[tuple]):
    """
        DBLoader의 sendquery를 사용하여 데이터를 한 줄씩 적재하는 함수
    """
    if not indata:
        print("적재할 데이터가 없습니다.")
        return

    # 테이블 초기화 (기존 테이블 삭제 및 생성)
    # 기존 테이블 삭제
    DBLoader.sendquery(f"DROP TABLE IF EXISTS {table_name}")

    # 새 테이블 생성
    attr_str = ", ".join(attributes)
    DBLoader.sendquery(f"CREATE TABLE IF NOT EXISTS {table_name} ({attr_str})")

    # 데이터 적재 (for 루프 활용)
    print(f"'{table_name}' 테이블에 데이터 적재 시작...")

    ls = []
    for row in indata:
        # SQL에 들어갈 수 있도록 데이터 포맷팅
        # 문자열 데이터의 경우 따옴표('')가 필요하므로 각 항목을 처리해줍니다.
        # 예: (2024, '아반떼') -> "2024, '아반떼'"
        values_str = ", ".join([f"'{str(item)}'" if not (item in ['', "None", "Null", "NULL"]) else "NULL" for item in row])

        # insert query
        sq = f"INSERT INTO {table_name} VALUES ({values_str})"
        ls.append(sq)

    DBLoader.sendquerys_with_commit(ls)

    print(f"'{table_name}' 테이블에 총 {len(indata)}건 저장 완료!")

attrib_price = (
    "model_name varchar(50) PRIMARY KEY",
    "price_min varchar(10)",
    "price_max varchar(10)",
    "ref_link TEXT"
)

attrib_oil = (
    "model_name varchar(50) PRIMARY KEY",
    "comp_name varchar(20) NOT NULL",
    "fuel_type varchar(20) NOT NULL",
    "fuel_eff_mix varchar(20) NOT NULL",
    "fuel_eff_cty varchar(20) NOT NULL",
    "fuel_eff_hw varchar(20) NOT NULL",
    "run_per_charge varchar(20)",
    "estm_fuel_price varchar(20) NOT NULL",
    "car_class varchar(10) NOT NULL",
    "displacement varchar(10)",
    "release_year varchar(10) NOT NULL",
    "price_model varchar(50)",
    "FOREIGN KEY (price_model) REFERENCES car_price(model_name)"
)

# --- 실행부 ---
if __name__ == "__main__":
    DBLoader.sendquery("DROP TABLE IF EXISTS car_oil")
    DBLoader.sendquery("DROP TABLE IF EXISTS car_price")

    export_table("car_price", attrib_price, csv_import("data/vehicles/car_price.csv"))
    export_table("car_oil", attrib_oil, csv_import("data/vehicles/car_oil.csv"))