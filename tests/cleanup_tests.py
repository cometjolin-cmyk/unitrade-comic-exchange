import os
import shutil

TEST_DIR = "/Users/comet/.gemini/antigravity/scratch/網頁設計1/tests"

def cleanup():
    """
    清除測試執行過程中產生的暫存快取檔案，並重設測試狀態。
    保留 test_matrix.json, synthetic_dataset_100.json 與 TEST_REPORT.md 作為交件佐證。
    """
    temp_files = [
        os.path.join(TEST_DIR, "_temp_runner.js"),
        os.path.join(TEST_DIR, "__pycache__")
    ]
    
    cleaned = []
    for item in temp_files:
        if os.path.isfile(item):
            os.remove(item)
            cleaned.append(item)
        elif os.path.isdir(item):
            shutil.rmtree(item)
            cleaned.append(item)

    print("=== 測試環境清理完成 ===")
    if cleaned:
        for c in cleaned:
            print(f"已清除暫存：{c}")
    else:
        print("目前無暫存垃圾檔案需要清除，測試環境保持極致整潔！")
    print("若欲在瀏覽器中重設使用者的 localStorage 收藏與刊登資料：")
    print("請在瀏覽器 Console 執行：localStorage.clear(); location.reload();")

if __name__ == "__main__":
    cleanup()
