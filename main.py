import telegram.ext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler


def get_bienso(timbienso):
    file = open("CSDL.csv", mode="r", encoding="utf-8")
    header = file.readline()
    row = file.readline()
    while row != "":
        row_list = row.split(";")
        if row_list[2] == timbienso:
            ketqua = row_list
            return ketqua
            break
        else:  row = file.readline()
    else:
        return 0
def get_sdt(timsdt):
    file = open("CSDL.csv", mode="r", encoding="utf-8")
    header = file.readline()
    row = file.readline()
    while row != "":
        row_list = row.split(";")
        if row_list[8]== timsdt:
            ketqua = row_list
            return ketqua
            break
        else:  row = file.readline()
    else:
        return 0
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""
        'Các lệnh\n'
        /bs => Tra cứu biển số ví dụ: /bs 98A.121.38
        /sdt => Tra cứu theo số điện thoại vd: /sdt 0985733437
        Phí tra cứu: Hiện tại Free
        """)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Mời Anh {update.effective_user.full_name} xơi')
async def bs (update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
    n=context.args[0]
    databs = get_bienso(n)
    if databs==0:
        await update.message.reply_text(f'Không có thông tin')
    else:
        await update.message.reply_text(f'Thông tin biển số: {databs[2]},\n   Nhãn hiệu:{databs[3]}\n   Màu Sơn: {databs[4]} \n   Số chỗ ngồi: {databs[5]}\n   Chủ phương tiện: {databs[6]}\n   Địa chỉ: {databs[7]}\n   Số điện thoại: {databs[8]}')
async def sdt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    n1=context.args[0]
    datasdt = get_sdt(n1)
    if datasdt == 0:
        await update.message.reply_text(f'Không có thông tin')
    else:
        await update.message.reply_text(f'Thông tin biển số đăng ký số điện thoại: {datasdt}')
                                  #  f' Nhãn hiệu:{datasdt[3]}\n   Màu Sơn: {datasdt[4]} \n   Số chỗ ngồi: {datasdt[5]}\n   Chủ phương tiện: {datasdt[6]}\n   Địa chỉ: {datasdt[7]}\n   Số điện thoại: {datasdt[8]}')



app = ApplicationBuilder().token("6190359096:AAGDCJ0UmcVIqIz0JK9PDEgHMlxiQ56JI0o").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("bs", bs))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("sdt", sdt))

app.run_polling()