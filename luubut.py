from email.message import EmailMessage
import random
import smtplib
import streamlit as st


def gui_email(ten_nguoi_gui, phan_hoi):
    try:
        email_user = st.secrets["EMAIL_USER"]
        email_password = st.secrets["EMAIL_PASSWORD"]

        msg = EmailMessage()
        msg["Subject"] = f"Lưu bút từ {ten_nguoi_gui}"
        msg["From"] = email_user
        msg["To"] = email_user
        msg.set_content(f"Người gửi: {ten_nguoi_gui}\n\nNội dung: {phan_hoi}")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_user, email_password)
            smtp.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Lỗi chi tiết: {e}")
        return False


data_hoc_sinh = {
    ("Trần Lê Bảo Ngọc", "02/07/2008"): {
        "ma": "BN08D5",
        "loi_chuc": (
            "T ít nch với m quá nên t cũng chả bíc nói gì, nma tại m xinh nên t"
            " sẽ viết cgi đấy, chúc m đỗ đh nháa"
        ),
    },
    ("Nguyễn Hải Nhi", "13/09/2008"): {
        "ma": "HN08D5",
        "loi_chuc": (
            "Hê lô hê lô, quà m tặng t còn chưa lắp xong nữa, thui thì để thi"
            " đh xong ik kkk, chúc cô giáo Hải Nhi thi tốt nhá, m là bạn cùng"
            " bàn mà t quý nhất trong tất cả bạn cùng bàn đấy hihihihi"
        ),
    },
    ("Nguyễn Yến Nhi", "08/06/2008"): {
        "ma": "YN08D5",
        "loi_chuc": (
            "=)))))) tại m giống Mona Lisa(có thêm lông mày) nên t siêu ấn"
            " tượng, t quyết định viết cho m, chúc m thi tốt, cgi cũng tốt 100%"
            " nhá kkk"
        ),
    },
    ("Cùng Việt Phương", "20/10/2008"): {"ma": "VP08D5", "loi_chuc": ""},
    ("Nguyễn Thị Phương Thảo", "23/06/2008"): {
        "ma": "PT08D5",
        "loi_chuc": (
            "Đồng ăn mảnh của t, t rất sốc khi nghe m chọn đc ngành và bây giờ"
            " vẫn ko ngừng sốc, thôi thì chúc Thảo thi siêu tốt ước gì được"
            " nấy nhá. Thi nhanh lên còn đi chơi với t nữa, với cả lên đh ít"
            " ngủ thôi. Hồi đầu lớp 10 vào t ấn tượng m vì m ngồi với mtrg, t"
            " thấy sợ và t nghĩ ko nên chơi với 2 bm, ai ngờ m lại là mẹ 2 con"
            " lúc nào cũng buồn ngủ, hihihi thao gay thao gay thao gay thao gay"
            " thao gay thao gay thao gay"
        ),
    },
    ("Trần Bảo Thy", "19/08/2008"): {
        "ma": "BT08D5",
        "loi_chuc": (
            " hihi t bị ấn tượng cái lúc t với m đi bán đồ ở kỉ niệm 30 năm"
            " của trường ý=))))))))) nhớ mãi, chúc m thi đh siêu tốt trúng nv 1"
            " nha hahahaahahahah"
        ),
    },
    ("Nguyễn Hiền Trang", "17/10/2008"): {
        "ma": "HT08D5",
        "loi_chuc": (
            " kcj để nói, quá chán, lên đh ngủ ít thôi b nhá, lo mà học đi, 3"
            " năm c3 ngày nào cũng ngủ. Thi vẽ cho tốt rồi học t còn đc gặp"
            " người nổi tiếng nhớ ch=)))). Viết thêm nè, t ấn tượng với m tại m"
            " cùng chung cư với t, người bạn đầu tiên gần nhà t đến thế nên t"
            " thích m lắm hihi. Htrg gay htrg gay htrg gay, tên hàng chiên là t"
            " gọi m đấy ko phải mtrg đâu htrg gay htrg gay htrg gay"
        ),
    },
    ("Đoàn Minh Trang", "01/09/2008"): {
        "ma": "MT08D5",
        "loi_chuc": (
            "Dnay t với bím nch nhiều qtqđ, sắp thi đh xong nghỉ chơi rồi, bím"
            " nhớ yêu Quốc Long lâu lâu vào nhá=))) Đỗ rồi nên ko cần học đâu"
            " cũng ko chúc gì hết leuleuleu, mtrg yêu qlong mtrg yêu qlong mtrg"
            " yêu qlong mtrg yêu qlong mtrg yêu qlong mtrg yêu qlong mtrg yêu"
            " qlong. Lên đh đừng có sếch dốc với mấy bạn đh nha, cac b ko thích"
            " đâu. Viết cho dài ra thì hồi trc t sợ  vl kbt s trông m cứ angry"
            " mà bây giờ cứ ngáo ngáo"
        ),
    },
    ("Nguyễn Lê Bảo Trâm", "09/10/2008"): {
        "ma": "BT08D5",
        "loi_chuc": (
            "Đề nghị m chở t đi học đến khi t sang Hàn luôn để sau đỡ nhớ t"
            " heh, chúc bím thi hsa với thi đh siêu tôt nhá, trúng nv1, với chọn"
            " ngành nhanh lên t còn biết. Viết thêm nè, mới vào lớp 10 t  chả"
            " ấn tượng gì với m cả, chỉ biết m chơi với htrg thôi hihi. Ai mà"
            " ngờ ae mình lại đi xe với nhau hết năm c3 thân cỡ dó, m phải sang"
            " Hàn chơi với t 1 lần nha bím btram gay tram gay tram gay tram gay"
            " tram ay tram gay tram gay tram gay"
        ),
    },
    ("Lê Bảo Trân", "28/10/2008"): {
        "ma": "BT08D5",
        "loi_chuc": (
            "Hihihihi, sắp hết năm rồi đỡ phải làm lớp trưởng, mệt phết nhỉ,"
            " chúc lớp trưởng thi đh tốt ước gì đc nấy nhe, "
        ),
    },
    ("Phạm Đặng Tuệ Trân", "14/02/2008"): {
        "ma": "TTD5",
        "loi_chuc": (
            "T vẫn thích Tuệ Trân đi du học với t đó, hihihi,  chúc Tuệ Trân"
            " đỗ nv 1 và làm nhiều bánh cho t hihi, lên đh nhớ nói nhiều lên"
            " nhá"
        ),
    },
    ("Vũ Thanh Trúc", "19/04/2008"): {
        "ma": "TT08D5",
        "loi_chuc": (
            "Chúc Trúc thích gì là đỗ hết sạch luôn, lúc đầu chưa nch t còn sợ"
            " m cơ khs=))))) thôi cố lên nhá Trúc, trông tỉ lệ m đỗ chắc cỡ"
            " 99,99% ý"
        ),
    },
    ("Trương Nguyễn Hà Vy", "20/02/2008"): {
        "ma": "HV08D5",
        "loi_chuc": (
            "Top 1 điều sốc nhất là t với m nói chuyện với nhau đấy=)))) giờ"
            " vẫn bất ngờ, t kbt m học ngành gì nma chúc Hà Vy thích ngành gì"
            " là đỗ hết sạch=)))"
        ),
    },
    ("Hoàng Lan Anh", "21/07/2008"): {
        "ma": "LA08D5",
        "loi_chuc": (
            "May mà Lan Anh học địa với t đấy hahahah, chúc cô giáo Lan Anh"
            " đỗ trường mình muốn nhá"
        ),
    },
    ("Nguyễn Thị Trâm Anh", "10/02/2008"): {
        "ma": "TA08D5",
        "loi_chuc": (
            "Chúc Trâm Anh siêu cấp đáng iu trúng tuyển ngành mình muốn nè, thi"
            " nhanh lên chúng mình còn đi ăn nữa=)))))))))))"
        ),
    },
    ("Mai Thiên Bảo Anh", "18/02/2008"): {
        "ma": "BA08D5",
        "loi_chuc": (
            "T thấy m chăm vl, ước gì t cũng đc 1 phần như m là ngon rồi, t"
            " thấy kiểu gì m cũng đỗ ngành m muốn nma t chúc m đỗ đc nv cao"
            " nhất của m=))"
        ),
    },
    ("Dương Bảo Quốc", "28/12/2008"): {
        "ma": "BQ08Q2",
        "loi_chuc": (
            "Hihihihihi, ko ngờ là t đc nch lại với  m đấy, trc t thấy có lỗi"
            " với m phết hihi, t muốn ae mình thân nhau hơn và thân siêu lâu"
            " nữa, có chuyện gì thì m phải kể bọn t nhá. Cuối tháng 5 này"
            " phỏng vấn cho tốt vào, phải 100% đỗ du học nhá=)) ước gì m đỗ"
            " để ae mình còn đi chơi kkk"
        ),
    },
    ("Nguyễn Trung Nghĩa", "30/09/2008"): {
        "ma": "TN08Q2",
        "loi_chuc": (
            "Ae mình chơi lâu qtqđ, chắc t chơi với  m với pl với quốc lâu mà"
            " dai nhất trong lớp mình rồi đó=))), t muốn ae mình thân lâu hơn"
            " nữa, t thích m kể mấy cái chuyện của m lắm tại t bị tọc mạch,"
            " m chắc chắn phải đỗ FTU để ae mình còn đi chơi vui vẻ đấy nhá"
            " nhớ chưa nhớ chưa"
        ),
    },
    ("Trần Ngọc Phương Linh", "02/02/2008"): {
        "ma": "PL08Q2",
        "loi_chuc": (
            "hihihihi, tớ muốn chúng mình sẽ chơi với nhau thật lâu, PLinh nhất định phải đỗ HLU"
            " đók=))) xong rồi ae mình còn đi chơi nhiều nhiều nữa với chơi"
            " roblox=D"
        ),
    },
    ("Đậu Ngọc Linh", "17/03/2008"): {"ma": "NL08D5", "loi_chuc": " chúc Linh đỗ được trường đại học mình mong muốn và luôn chơi với nhau nhe "},
    ("Nguyễn Trần Phương Anh", "21/11/2008"): {
        "ma": "PA08Q2",
        "loi_chuc": (
            "Lâu rồi không gặp cậu, Phanh học giỏi thế tớ nghĩ là 99,99% đỗ"
            " nv 1 kkk, nma dù sao cũng chúc cậu thi đỗ nv 1 rồi ae mình đi chơi"
            " nho hihi"
        ),
    },
    ("Nguyễn Trúc An", "18/05/2008"): {
        "ma": "TA08Q2",
        "loi_chuc": (
            "Siêu lâu rồi ko gặp An, mình cũng ít nói chuyện nữa, chúc An thi đỗ NEU"
            " nhasaaaa kkkkk"
        ),
    },
    ("Nguyễn Phan Hà Anh", "30/04/2008"): {
        "ma": "HA08Q2",
        "loi_chuc": (
            "Lâu rồi không gặp cậu, chúc Hà Anh thi đỗ trường đh ngành mình"
            " muốn nhá hahahahaahahaha"
        ),
    },
    ("Lê Hạnh Linh", "07/01/2008"): {
        "ma": "HL08Q2",
        "loi_chuc": (
            "Như kiểu 100 năm rồi ko gặp ý=))) may mà có Hlinh lấy sổ đoàn cho"
            " tớ tớ mưới đc đi thi đh hehe, chúc HLinh thi gì trúng nấy kkk"
        ),
    },
    ("Đặng Trung Nghĩa", "02/12/2008"): {
        "ma": "DN08Q2",
        "loi_chuc": (
            "T với m chơi lâu phết đók, kiểu ae mình ko bị mất liên lạc ý"
            " ahihi=))) t cảm ơn m đã nghe mấy chuyện linh tinh của t nha, m"
            " là người t thích tâm sự nhất tại m nói gì nghe cũng lọt tai t"
            " á=)) mong là t với m có thể chơi lâu. Uowsc gì m đỗ NEU để ae"
            " mình được đi chơi nhiều nhiều, vui vẻ, nhất định phải cố 100%"
            " đó nha"
        ),
    },
    ("Trần Đức Huy", "30/08/2008"): {
        "ma": "DH08Q2",
        "loi_chuc": (
            " Web này là t code đó, kinh chưa, t ngồi từ 12h trưa đến bh là"
            " 11h30 tối=))), cảm ơn m vì t hỏi gì m cũng rep nhaa, quý lắm ý"
            " mặc dù m k rep t, lúc m mời t đi kỉ yếu t bất ngờ vl. T thấy"
            " học hành của m có gì để chê nữa rồi nên  chúc m cái gì cũng"
            " thành công ha."
        ),
    },
    ("Hong Eun Woo", "22/12/2005"): {
        "ma": "EW05Q2",
        "loi_chuc": (
            " Hihihi, me cảm ơn vì lúc nào cũng nhiệt tình giúp me nha kkk,"
            " chúc u thi đại học điểm siêu siêu cao, đạt học bổng BUV 100% nha"
            " kkk"
        ),
    },
    ("Phạm Khánh Minh", "02/10/2008"): {
        "ma": "KM08Q2",
        "loi_chuc": (
            " Hihihihi, chúc Khánh Minh đỗ nv 1 nha, hình như là NEU nhỉii với"
            " cảm ơn KM đến kỉ yếu của tớ nha kkkk. Lên c3 ae mình ít gặp nhau"
            " quá trời làm tớ nhớ hồi trc tớ với cậu với đnghia đi xe bus vui"
            " qtqđ hahahah, chúc KMinh ước gì cũng đc hehe"
        ),
    },
    ("Phan Minh Thủy", "23/03/2008"): {
        "ma": "MT08Q2",
        "loi_chuc": (
            " I hope you get accepted into the HASS division at UIC Yonsei."
        ),
    },
}

danh_sach_loi_chuc_uic = [
    (
        "Hello! Wishing you a wonderful and relaxing day ahead. As a CTM"
        " applicant, I designed this interactive web app to blend technology"
        " with human-centric communication—even writing a custom Python script"
        " to dynamically greet guest evaluators like you. I hope it brings a"
        " smile to your face!"
    ),
    (
        "Hi there! Have a fantastic day! If you're reading this personalized"
        " message, it means my Streamlit app successfully ran its fallback"
        " routing to create a seamless UX for the HASS admissions team. Thank"
        " you so much for taking the time to explore my digital guestbook!"
    ),
    (
        "Welcome! Hope you're having an amazing and energetic day. This project"
        " reflects my passion for Communication and Technology Management—I"
        " specifically coded a dynamic branch to surprise visitors like you and"
        " make your evaluation experience more engaging!"
    ),
    (
        "Hello! Wishing you a lovely day filled with good energy. Surprise!"
        " Behind this clean interface lies a blend of Python automation and UX"
        " design tailored for the Yonsei HASS team. Thanks for dropping by to"
        " see how I bridge tech and human connection—hope you love it!"
    ),
    (
        "Hi! Have a great day ahead. As you test out this application, I"
        " thought you'd appreciate knowing that I programmed a dedicated"
        " exception rule for evaluators, reflecting my interest in interactive"
        " digital media. So glad you're here to experience my work!"
    ),
]

st.title("My digital guestbook")
st.write("Please enter your full information.")

ten = st.text_input("Full nameee pleaseee")
ngay_sinh = st.text_input(
    "I would also like to know more about your date of birth( dd/mm/yyyy):"
)

if "step" not in st.session_state:
    st.session_state.step = 1

if st.button("click hear to find your own code"):
    if ten:
        st.session_state.ten_nguoi_gui = ten
    else:
        st.session_state.ten_nguoi_gui = "Người ẩn danh"

    key = (ten.strip(), ngay_sinh.strip())

    if key in data_hoc_sinh:
        st.session_state.info = data_hoc_sinh[key]
        st.success(
            "Good news, your own message by my own heart is already=)))))"
        )
    else:
        if "2008" not in ngay_sinh:
            st.success(
                f"Welcome {ten}! The system has prepared a dedicated experience code for UIC Yonsei."
            )
            st.session_state.info = {
                "ma": "UICSPRING27",
                "loi_chuc": random.choice(danh_sach_loi_chuc_uic),
            }
        else:
            st.warning("Please wait a second=)))...")
            st.session_state.info = {
                "ma": "0852DQ",
                "loi_chuc": (
                    "Ae mình gặp được nhau là siêu có duyên đó, nhớ nha, chúc thi"
                    " đh tốt đạt nv 1 nhooo kkkk"
                ),
            }

    st.session_state.step = 2

# --- HIỆN MÃ CODE ---
if st.session_state.step >= 2:
    st.write("Hmmmm ur code is.... ( copy the code to unlock plss :) )")
    st.code(st.session_state.info["ma"])

if st.session_state.step == 2:
    ma_nhap = st.text_input(
        "Hmmmm ur code is....( copy the code to unlock plss :) )",
        type="password",
        key="input_ma_nhap",
    )

    if st.button("Unlockkk..."):
        if ma_nhap == st.session_state.info["ma"].strip():
            # Kích hoạt hiệu ứng bóng bay
            st.balloons()
            # Đánh dấu trạng thái đã mở khóa để hiển thị nội dung bên dưới ngay lập tức
            st.session_state.da_mo_khoa = True
        else:
            st.error("Incorrecttt")

# Hiển thị nội dung lời chúc và ô gửi email khi đã nhập đúng mã
if st.session_state.get("da_mo_khoa", False):
    if "info" in st.session_state:
        st.info(
            f" {st.session_state.info.get('loi_chuc', 'Chúc bạn thành công!')}"
        )

    st.divider()

    phan_hoi = st.text_area(
        "You can write something or not—just don't write anything"
        " sappy🤧, okay? :)))",
        key="txt_phan_hoi",
    )
    if st.button("Drop Thủy a quick note😗=)))))"):
        if phan_hoi:
            ten_gui = st.session_state.get("ten_nguoi_gui", "Người lạ")
            if gui_email(ten_gui, phan_hoi):
                st.success("Sent successfully, tksss✌")
            else:
                st.error("error occurred while sending the email❌✍🏻")
        else:
            st.warning(
                "You have to ✏️ something to send it, you can't send it if you"
                " leave it blank."
            )
