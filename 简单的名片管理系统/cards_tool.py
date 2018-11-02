# 记录所有名字的字典
cards_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统V1.0】")
    print(" ")
    print("1:新建名片")
    print("2:显示全部名片")
    print("3:搜索名片")
    print("")
    print("0:退出系统")
    print("*" * 50)
    print("")


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1 用户输入详细名片信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")

    # 2 用户输入的信息建立一个字典
    card_dic = {
        "name": name_str,
        "phone": phone_str,
        "QQ": qq_str,
        "email": email_str
    }
    # 3 把建立的字典加入列表中
    cards_list.append(card_dic)
    print(cards_list)
    print("添加名片成功")


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")
    print("*" * 50)
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t\t\t")
    print("")
    print("=" * 50)
    for cards in cards_list:
        print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (cards["name"],
                                              cards["phone"],
                                              cards["QQ"],
                                              cards["email"]))


def search_card():
    # print("-" * 50)
    # print("可选用的项目有：")
    # print("请输入搜索的项目：")
    # print("name")
    # print("phone")
    # print("QQ")
    # print("email")
    # search_info = input("请输入需要查询的项目：")
    # while search_info not in ["name", "phone", "QQ", "email"]:
    #     print("输入有误，请重新输入！")
    #     search_info = input("请输入需要查询的项目：")
    # else:
    #     print("输入正确！")
    #     search_detail = input("请输入需要查询的信息：")
    #     for search in cards_list:
    #         if search[search_info] == search_detail:
    #             print(search)
    #         else:
    #             print("没有找到！")
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    # 提示用户输入要搜索的姓名
    find_name = input("请输入姓名：")

    # 遍历名片列表，查询要搜索的姓名
    for find in cards_list:
        if find["name"] == find_name:
            for name in ["姓名", "电话", "QQ", "邮箱"]:
                print(name, end="\t\t")
            print("")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (find["name"],
                                            find["phone"],
                                            find["QQ"],
                                            find["email"]))
            deal_cards(find)
            break
    else:
        print("没有找到%s！" % find_name)


def delete_card():
    """删除名片"""
    print("-" * 50)
    print("删除名片")


def deal_cards(find_card):
    """

    :param find_card:处理的字典
    :return:没有返回
    """
    print("你想进行什么操作！")
    print("")
    print("1:删除该名片！")
    print("")
    print("2:修改名片")
    print("")
    print("0:返回主界面")
    action_card = input("请输入：")
    if action_card in ["1", "2"]:
        if action_card == "1":
            cards_list.remove(find_card)
            print("删除名片成功！")
        elif action_card == "2":
            find_card["name"] = input_cardInfo(find_card["name"], "请输入需要修改的姓名：")
            find_card["phone"] = input_cardInfo(find_card["phone"], "请输入需要修改的电话：")
            find_card["QQ"] = input_cardInfo(find_card["QQ"], "请输入需要修改的QQ：")
            find_card["email"] = input_cardInfo(find_card["email"], "请输入需要修改的邮箱：")
            print("修改名片成功！")


def input_cardInfo(dict_value, tipMessage):
    """
    :param dict_value: 字典中原有的值
    :param tipMessage: 输入的文字提示
    :return:按Enter返回字典原有的值
            否则返回输入的内容。
    """
    change_cardInfo = input(tipMessage)
    if len(change_cardInfo) > 0:
        return change_cardInfo
    else:
        return dict_value
