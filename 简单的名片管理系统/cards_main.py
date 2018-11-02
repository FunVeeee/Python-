import cards_tool

while True:
    # 显示功能菜单
    cards_tool.show_menu()
    action_str = input("请你选择需要的操作：")
    print("你选的的操作是【%s】" % action_str)
    # 1,2,3针对名片的操作
    if action_str in ["1", "2", "3"]:

        # TODO 增加名片
        if action_str == "1":
            cards_tool.new_card()

        # TODO 显示全部名片
        elif action_str == "2":
            cards_tool.show_all()

        # TODO 查询名片
        elif action_str == "3":
            cards_tool.search_card()


    # 退出系统操作
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】！")
        break
    # 输入内容错误
    else:
        print("输入错误，请重新输入！")
