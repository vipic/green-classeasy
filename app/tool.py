def pick(id, data):
    try:
        ans = [obj for obj in data if id == obj["id"]][0]

        images = []
        desc = ""
        for units in ans["units"]:
            for entries in units["entries"]:
                if entries["t"] == "Upload":
                    images += entries["value"]
                if entries["t"] == "TextArea" and not entries["value"] == "":
                    desc += entries["value"] + "\n --- \n"

        return {
            "base_path": ans["base_url"],
            "folder": ans["publish_time"],
            "images": images,
            "desc": desc
        }
    except Exception as e:
        print(e)
        return {}
