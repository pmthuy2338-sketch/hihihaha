import streamlit as st
import smtplib
from email.message import EmailMessage

def gui_email(ten_nguoi_gui, phan_hoi):
    try:
        email_user = st.secrets["EMAIL_USER"]
        email_password = st.secrets["EMAIL_PASSWORD"]
        
        msg = EmailMessage()
        msg['Subject'] = f"Lưu bút từ {ten_nguoi_gui}"
        msg['From'] = email_user
        msg['To'] = email_user 
        msg.set_content(f"Người gửi: {ten_nguoi_gui}\n\nNội dung: {phan_hoi}")
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_user, email_password)
            smtp.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Lỗi chi tiết: {e}") 
        return False
 
# --- DỮ LIỆU LỚP ---
data_hoc_sinh = {
     ("Trần Lê Bảo Ngọc", "02/07/2008"): {"ma": "BN08D5", "loi_chuc": "T ít nch với m quá nên t cũng chả bíc nói gì, nma tại m xinh nên t sẽ viết cgi đấy, chúc m đỗ đh nháa"},
     ("Nguyễn Hải Nhi", "13/09/2008"): {"ma": "HN08D5", "loi_chuc": "Hê lô hê lô, quà m tặng t còn chưa lắp xong nữa, thui thì để thi đh xong ik kkk, chúc cô giáo Hải Nhi thi tốt nhá, m là bạn cùng bàn mà t quý nhất trong tất cả bạn cùng bàn đấy hihihihi"},
     ("Nguyễn Yến Nhi", "08/06/2008"): {"ma": "YN08D5", "loi_chuc": "=)))))) tại m giống Mona Lisa(có thêm lông mày) nên t siêu ấn tượng, t quyết định viết cho m, chúc m thi tốt, cgi cũng tốt 100% nhá kkk"},
     ("Cùng Việt Phương", "20/10/2008"): {"ma": "VP08D5", "loi_chuc": ""},
     ("Nguyễn Thị Phương Thảo", "23/06/2008"): {"ma": "PT08D5", "loi_chuc": "Đồng ăn mảnh của t, t rất sốc khi nghe m chọn đc ngành và bây giờ vẫn ko ngừng sốc, thôi thì chúc Thảo thi siêu tốt ước gì được nấy nhá. Thi nhanh lên còn đi chơi với t nữa, với cả lên đh ít ngủ thôi. Hồi đầu lớp 10 vào t ấn tượng m vì m ngồi với mtrg, t thấy sợ và t nghĩ ko nên chơi với 2 bm, ai ngờ m lại là mẹ 2 con lúc nào cũng buồn ngủ, hihihi thao gay thao gay thao gay thao gay thao gay thao gay thao gay"},
     ("Trần Bảo Thy", "19/08/2008"): {"ma": "BT08D5", "loi_chuc": " hihi t bị ấn tượng cái lúc t với m đi bán đồ ở kỉ niệm 30 năm của trường ý=))))))))) nhớ mãi, chúc m thi đh siêu tốt trúng nv 1 nha hahahaahahahah"},
     ("Nguyễn Hiền Trang", "17/10/2008"): {"ma": "HT08D5", "loi_chuc": " kcj để nói, quá chán, lên đh ngủ ít thôi b nhá, lo mà học đi, 3 năm c3 ngày nào cũng ngủ. Thi vẽ cho tốt rồi học t còn đc gặp người nổi tiếng nhớ ch=)))). Viết thêm nè, t ấn tượng với m tại m cùng chung cư với t, người bạn đầu tiên gần nhà t đến thế nên t thích m lắm hihi. Htrg gay htrg gay htrg gay, tên hàng chiên là t gọi m đấy ko phải mtrg đâu htrg gay htrg gay htrg gay"},
     ("Đoàn Minh Trang", "01/09/2008"): {"ma": "MT08D5", "loi_chuc": "Dnay t với bím nch nhiều qtqđ, sắp thi đh xong nghỉ chơi rồi, bím nhớ yêu Quốc Long lâu lâu vào nhá=))) Đỗ rồi nên ko cần học đâu cũng ko chúc gì hết leuleuleu, mtrg yêu qlong mtrg yêu qlong mtrg yêu qlong mtrg yêu qlong mtrg yêu qlong mtrg yêu qlong mtrg yêu qlong. Lên đh đừng có sếch dốc với mấy bạn đh nha, cac b ko thích đâu. Viết cho dài ra thì hồi trc t sợ  vl kbt s trông m cứ angry mà bây giờ cứ ngáo ngáo"},
     ("Nguyễn Lê Bảo Trâm", "09/10/2008"): {"ma": "BT08D5", "loi_chuc": "Đề nghị m chở t đi học đến khi t sang Hàn luôn để sau đỡ nhớ t heh, chúc bím thi hsa với thi đh siêu tôt nhá, trúng nv1, với chọn ngành nhanh lên t còn biết. Viết thêm nè, mới vào lớp 10 t  chả ấn tượng gì với m cả, chỉ biết m chơi với htrg thôi hihi. Ai mà ngờ ae mình lại đi xe với nhau hết năm c3 thân cỡ dó, m phải sang Hàn chơi với t 1 lần nha bím btram gay tram gay tram gay tram gay tram ay tram gay tram gay tram gay tram gay"},
     ("Lê Bảo Trân", "28/10/2008"): {"ma": "BT08D5", "loi_chuc": "Hihihihi, sắp hết năm rồi đỡ phải làm lớp trưởng, mệt phết nhỉ, chúc lớp trưởng thi đh tốt ước gì đc nấy nhe, "},
     ("Phạm Đặng Tuệ Trân", "14/02/2008"): {"ma": "TTD5", "loi_chuc": "T vẫn thích Tuệ Trân đi du học với t đó, hihihi,  chúc Tuệ Trân đỗ nv 1 và làm nhiều bánh cho t hihi, lên đh nhớ nói nhiều lên nhá"},
     ("Vũ Thanh Trúc", "19/04/2008"): {"ma": "TT08D5", "loi_chuc": "Chúc Trúc thích gì là đỗ hết sạch luôn, lúc đầu chưa nch t còn sợ m cơ khs=))))) thôi cố lên nhá Trúc, trông tỉ lệ m đỗ chắc cỡ 99,99% ý"},
     ("Trương Nguyễn Hà Vy", "20/02/2008"): {"ma": "HV08D5", "loi_chuc": "Top 1 điều sốc nhất là t với m nói chuyện với nhau đấy=)))) giờ vẫn bất ngờ, t kbt m học ngành gì nma chúc Hà Vy thích ngành gì là đỗ hết sạch=)))"},
     ("Hoàng Lan Anh", "21/07/2008"): {"ma": "LA08D5", "loi_chuc": "May mà Lan Anh học địa với t đấy hahahah, chúc cô giáo Lan Anh đỗ trường mình muốn nhá"},
     ("Nguyễn Thị Trâm Anh", "10/02/2008"): {"ma": "TA08D5", "loi_chuc": "Chúc Trâm Anh siêu cấp đáng iu trúng tuyển ngành mình muốn nè, thi nhanh lên t với m còn đi ăn nữa=)))))))))))"},
     ("Mai Thiên Bảo Anh", "18/02/2008"): {"ma": "BA08D5", "loi_chuc": "T thấy m chăm vl, ước gì t cũng đc 1 phần như m là ngon rồi, t thấy kiểu gì m cũng đỗ ngành m muốn nma t chúc m đỗ đc nv cao nhất của m=))"},
     ("Dương Bảo Quốc", "28/12/2008"): {"ma": "BQ08Q2", "loi_chuc": "Hihihihihi, ko ngờ là t đc nch lại với  m đấy, trc t thấy có lỗi với m phết hihi, t muốn ae mình thân nhau hơn và thân siêu lâu nữa, có chuyện gì thì m phải kể bọn t nhá. Cuối tháng 5 này phỏng vấn cho tốt vào, phải 100% đỗ du học nhá=)) ước gì m đỗ để ae mình còn đi chơi kkk"},     ("Nguyễn Trung Nghĩa", "30/09/2008"): {"ma": "TN08Q2", "loi_chuc": "Ae mình chơi lâu qtqđ, chắc t chơi với  m với pl với quốc lâu mà dai nhất trong lớp mình rồi đó=))), t muốn ae mình thân lâu hơn nữa, t thích m kể mấy cái chuyện của m lắm tại t bị tọc mạch, m chắc chắn phải đỗ FTU để ae mình còn đi chơi vui vẻ đấy nhá nhớ chưa nhớ chưa"},
     ("Trần Ngọc Phương Linh", "02/02/2008"): {"ma": "PL08Q2", "loi_chuc": "hihihihi, tớ muốn tớ với cậu chơi siêu siêu lâu, chả biết PLinh định học ngành gì nhưng mà PLinh phải phải nhất định phải đỗ đók=))) xong rồi ae mình còn đi chơi nhiều nhiều nữa với chơi roblox=D"},     ("Đậu Ngọc Linh", "17/03/2008"): {"ma": "NL08D5", "loi_chuc": ""},
     ("Nguyễn Trần Phương Anh", "21/11/2008"): {"ma": "PA08Q2", "loi_chuc": "Lâu rồi không gặp cậu, Phanh học giỏi thế tớ nghĩ là 99,99% đỗ nv 1 kkk, nma dù sao cũng chúc cậu thi đỗ nv 1 rồi ae mình đi chơi nho hihi"},
     ("Nguyễn Trúc An", "18/05/2008"): {"ma": "TA08Q2", "loi_chuc": "Siêu lâu rồi ko gặp An, mình cũng ít nch nữa, chúc An thi đỗ NEU nhasaaaa kkkkk"},
     ("Nguyễn Phan Hà Anh", "30/04/2008"): {"ma": "HA08Q2", "loi_chuc": "Lâu rồi không gặp cậu, chúc Hà Anh thi đỗ trường đh ngành mình muốn nhá hahahahaahahaha"},
     ("Lê Hạnh Linh", "07/01/2008"): {"ma": "HL08Q2", "loi_chuc": "Như kiểu 100 năm rồi ko gặp ý=))) may mà có Hlinh lấy sổ đoàn cho tớ tớ mưới đc đi thi đh hehe, chúc HLinh thi gì trúng nấy kkk"},
     ("Đặng Trung Nghĩa", "02/12/2008"): {"ma": "DN08Q2", "loi_chuc": "T với m chơi lâu phết đók, kiểu ae mình ko bị mất liên lạc ý ahihi=))) t cảm ơn m đã nghe mấy chuyện linh tinh của t nha, m là người t thích tâm sự nhất tại m nói gì nghe cũng lọt tai t á=)) mong là t với m có thể chơi lâu. Uowsc gì m đỗ NEU để ae mình được đi chơi nhiều nhiều, vui vẻ, nhất định phải cố 100% đó nha"),
     ("Trần Đức Huy", "30/08/2008"): {"ma": "DH08Q2", "loi_chuc": " Web này là t code đó, kinh chưa, t ngồi từ 12h trưa đến bh là 11h30 tối=))), cảm ơn m vì t hỏi gì m cũng rep nhaa, quý lắm ý mặc dù m k rep t, lúc m mời t đi kỉ yếu t bất ngờ vl. T thấy học hành của m có gì để chê nữa rồi nên  chúc m cái gì cũng thành công ha."),
     ("Hong Eun Woo", "22/12/2005"): {"ma": "EW05Q2", "loi_chuc": " Hihihi, me cảm ơn vì lúc nào cũng nhiệt tình giúp me nha kkk, chúc u thi đại học điểm siêu siêu cao, đạt học bổng BUV 100% nha kkk")
 }
 
st.title("Khôm phải là lưu bút")
st.write("Nhập thông tin mới hiện")

# --- FORM NHẬP LIỆU ---
ten = st.text_input("Đầy đủ họ tên nhs")
ngay_sinh = st.text_input("Đầy đủ ngày tháng năm sinh nè(ngày/tháng/năm sinh):")

if 'step' not in st.session_state:
    st.session_state.step = 1

if st.button("Bấm vô đây để tìm mã codeeeee"):
    # LƯU TÊN NGAY TẠI ĐÂY - Dù tìm thấy hay không thì vẫn lưu tên này lại
    if ten:
        st.session_state.ten_nguoi_gui = ten
    else:
        st.session_state.ten_nguoi_gui = "Người ẩn danh"

    key = (ten.strip(), ngay_sinh.strip())
    if key in data_hoc_sinh:
        st.session_state.info = data_hoc_sinh[key]
        st.success("Dìa dia thấy rồi hehehe")
    else:
        st.warning("Chờ một xíu nhaa")
        st.session_state.info = {"ma": "0852DQ", "loi_chuc": "Ae mình gặp được nhau là siêu có duyên đó, nhớ nha, chúc thi đh tốt đạt nv 1 nhooo kkkk"}
    
    st.session_state.step = 2

# --- HIỆN MÃ CODE ---
if st.session_state.step >= 2:
    st.write("Mã code của bạn là (copy lại để unlock nhé):")
    st.code(st.session_state.info['ma'])

# --- NHẬP MÃ ---
if st.session_state.step == 2:
    ma_nhap = st.text_input("Nhập mã code vào đây mới ra:", type="password")
    if st.button("Unlockkk..."):
        if ma_nhap == st.session_state.info["ma"]:
            st.balloons()
            st.info(f"{st.session_state.info['loi_chuc']}")
            st.session_state.step = 3
            st.rerun() 
        else:
            st.error("Nhập sai mã rồi, kém thế!!!")

# --- VIẾT PHẢN HỒI ---
if st.session_state.step == 3:
    
    if 'info' in st.session_state:
        st.info(f" {st.session_state.info.get('loi_chuc', 'Chúc bạn thành công!')}")
    
    st.divider() # Dòng kẻ ngang cho đẹp
    
    phan_hoi = st.text_area("Viết hoặc không viết cũm đc, đừng viết cái gì sến sến nhá=))):")
    if st.button("Gửi vài dòng cho Thủy đii=)))))"):
        if phan_hoi:
            # Dùng tên đã lưu trong session_state
            ten_gui = st.session_state.get('ten_nguoi_gui', 'Người lạ')
            if gui_email(ten_gui, phan_hoi):
                st.success("Đã gửi thành công, then kiu then kiu")
            else:
                st.error("Có lỗi xảy ra khi gửi mail")
        else:
            st.warning("Phải viết mới gửi đc=))) để trống ko gửi đc đâu")
    
    
