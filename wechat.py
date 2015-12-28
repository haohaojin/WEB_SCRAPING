import xml.dom.minidom

input_xml_string = "<xml><ToUserName><![CDATA[toUser]]></ToUserName><FromUserName><![CDATA[fromUser]]></FromUserName><CreateTime>1348831860</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[this is a test]]></Content><MsgId>1234567890123456</MsgId></xml>"


def get_tagname():
    doc = xml.dom.minidom.parseString(input_xml_string)
    collection = doc.documentElement
    toUserName = collection.getElementsByTagName("ToUserName")[0].childNodes[0].data
    fromUserName = collection.getElementsByTagName("FromUserName")[0].childNodes[0].data
    createTime = collection.getElementsByTagName("CreateTime")[0].childNodes[0].data
    msgType = collection.getElementsByTagName("MsgType")[0].childNodes[0].data
    content = collection.getElementsByTagName("Content")[0].childNodes[0].data
    msgId = collection.getElementsByTagName("MsgId")[0].childNodes[0].data


    print(toUserName)
    print(fromUserName)
    print(createTime)
    print(msgType)
    print(content)
    print(msgId)


get_tagname()
