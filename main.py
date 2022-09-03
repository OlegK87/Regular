import re

import csv

if __name__ == '__main__':

  pattern = r"(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*"
  substitution = r"+7(\2)\3-\4-\5 \6\7"

  with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

    def new_book(contact_list: list):
      new_contact_list = []
      for item in contact_list:
        full_name = ' '.join(item[:3]).split(' ')
        result = [full_name[0], full_name[1], full_name[2], item[3], item[4],
                  re.sub(pattern, substitution, item[5]),
                  item[6]]
        new_contact_list.append(result)
      return names(new_contact_list)


  def names(contacts: list):
    for contact in contacts:
      first_name = contact[0]
      last_name = contact[1]
      for new_contact_list in contacts:
        new_first_name = new_contact_list[0]
        new_last_name = new_contact_list[1]
        if first_name == new_first_name and last_name == new_last_name:
          if contact[2] == "":
             contact[2] = new_contact_list[2]
          if contact[3] == "":
             contact[3] = new_contact_list[3]
          if contact[4] == "":
             contact[4] = new_contact_list[4]
          if contact[5] == "":
             contact[5] = new_contact_list[5]
          if contact[6] == "":
             contact[6] = new_contact_list[6]

    result_list = []
    for i in contacts:
      if i not in result_list:
        result_list.append(i)

    return result_list

  with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_book(contacts_list))

