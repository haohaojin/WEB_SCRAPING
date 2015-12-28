import xml.dom.minidom


input_xml_string = "<xml><ToUserName><![CDATA[toUser]]></ToUserName><FromUserName><![CDATA[fromUser]]></FromUserName><CreateTime>1348831860</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[this is a test]]></Content><MsgId>1234567890123456</MsgId></xml>"

def get_tagname():
    doc = xml.dom.minidom.parseString(input_xml_string)
    for node in doc.getElementsByTagName("data"):
        print (node, node.tagName, node.getAttribute("version"))