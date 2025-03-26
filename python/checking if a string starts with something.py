def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'





def areYouPlayingBanjos(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";