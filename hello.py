import responder

api = responder.API()


@api.route("/")
def hello_world(req, resp):
    resp.text = "hello, world!"


@api.route("/hello/{who}")
def hello_to_who(req, resp, *, who):
    resp.text = f"hello, {who}!"


@api.route("/hello/{who}/json")
def hello_to_who_json(req, resp, *, who):
    resp.media = {"hello": who}


@api.route("/hello/{who}/html")
def hello_html(req, resp, *, who):
    resp.content = api.template('hello.json', who=who)


@api.route("/order_mail_confirm/{order_no}/json")
def order_mail_confirm_json(req, resp, *, order_no):
    mail = {"order_no": order_no,
            "last_name": "田中",
            "first_name": "大蔵",
            "last_name_kana": "たなか",
            "first_name_kana": "だいぞう",
            "shop_name": "大野庄三郎商店ネットストア",
            "order_date": "2018年12月11日 10時20分",
            "payment_limit": "2018年12月18日",
            "order_detail": ('1. 超すごい歯ブラシ\n'
                             '  単価：1,192円　×　数量：1　＝　商品代金：1,192円\n'
                             '  ギフト希望：なし'),
            "item_total_amount": 10000,
            "delivery_charge": 702,
            "cod_fee": 0,
            "used_point": 0,
            "total_amount": 10702,
            "payment_method": "コンビニ ローソン",
            "payment_method_notes": ('【お支払受付番号】　xxxxxx\n'
                                     '\n'
                                     '各コンビニエンスストアの支払い方法については下記をご参照ください。\n'
                                     '・ローソン\n'
                                     'https://example.com/cvs/lawson.html\n'
                                     '・セイコーマート\n'
                                     'https://example.com/cvs/seicomart.html\n'
                                     '・ファミリーマート\n'
                                     'https://example.com/cvs/famima.html\n'
                                     '・ミニストップ\n'
                                     'https://example.com/cvs/ministop.html'),
            "delivery_specification_date": "2018年12月13日",
            "delivery_specification_time": "午前中",
            "delivery_description": ('ご入金確認後、商品の確保・出荷をさせていただきます。\n'
                                     '商品の不具合や入荷遅延により、商品を早急にご用意できない場合、'
                                     'また状況により商品の注文をキャンセルさせていただく場合がございます。\n'
                                     '予めご了承くださいますようお願い申しあげます。\n'
                                     '詳細は、下記[ご利用ガイド]をご確認ください。\n'
                                     'https://example.com/guide/index.html'),
            "payment_description": ('ご入金期限日までに上記お支払金額をご指定いただいた'
                                    'コンビニエンスストアにてお支払ください。'),
            "cancel_or_change_description": ('※会員のお客様はご注文後、ご入金前でございましたら\n'
                                             'マイページよりご注文内容の一部変更が可能です。\n'
                                             'マイページはこちら\n'
                                             'https://example.com/mypage\n'
                                             '\n'
                                             'ご入金後の変更、キャンセルはできませんので\n'
                                             'あらかじめご了承くださいますようお願い申しあげます。'),
            "signature": ('　大野庄三郎商店ネットストアサービスセンター　　TEL：0123-45-7890\n'
                          '（月-金10：00-18：00　土日祝：休み）\n'
                          '【お問い合わせ】\n'
                          'https://example.com/netstore/inquiry')}

    message = api.template('mail_confirm.txt', **mail)
    subject = "【大野庄三郎商店ネットストア】ご注文ありがとうございます"
    address_from = "netstore@example.com"
    address_to = "d-tanaka@example.com"
    resp.media = {"order_no": order_no,
                  "subject": subject,
                  "address_from": address_from,
                  "address_to": address_to,
                  "message": message}


if __name__ == "__main__":
    api.run()
