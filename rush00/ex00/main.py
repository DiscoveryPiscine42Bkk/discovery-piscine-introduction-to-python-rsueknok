def show_menu():
    print("\n--- เมนูจัดการงานฟาร์ม ---")
    print("1. เพิ่มงานในฟาร์ม")
    print("2. แสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนงานในแต่ละประเภท")
    print("5. ออกจากโปรแกรม")

tasks = [] 
def add_task():
    name = input("ชื่องาน: ")
    category = input("ประเภท (เช่น พืช หรือ สัตว์): ")
    date = input("วันที่ (เช่น 2025-06-19): ")
    tasks.append({"name": name, "category": category, "date": date})
    print("✅ เพิ่มงานเรียบร้อยแล้ว")

def show_tasks():
    if not tasks:
        print("📭 ยังไม่มีงาน")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['name']} ({task['category']}) - วันที่: {task['date']}")

def delete_task():
    show_tasks()
    try:
        num = int(input("กรอกหมายเลขงานที่ต้องการลบ: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"🗑 ลบงาน '{removed['name']}' แล้ว")
        else:
            print("❌ หมายเลขไม่ถูกต้อง")
    except:
        print("❌ กรุณากรอกตัวเลข")

def summarize_tasks():
    summary = {}
    for task in tasks:
        category = task["category"]
        summary[category] = summary.get(category, 0) + 1
    print("📊 สรุปจำนวนงาน:")
    for category, count in summary.items():
        print(f"- {category}: {count} งาน")

while True:
    show_menu()
    choice = input("เลือกเมนู (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        summarize_tasks()
    elif choice == "5":
        print("👋 ออกจากโปรแกรมแล้ว")
        break
    else:
        print("❗ กรุณาเลือก 1-5 เท่านั้น")