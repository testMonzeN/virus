import webbrowser as WEB

class WEB:
    def web():
        Telegram = 'https://t.me/GhostBustGTA5'
        YouTube = 'https://www.youtube.com/channel/UCKfLWGq_gZGm40rzJhQii_w'
        Discord = 'https://discord.gg/wUAvuTUAPj'
        Steam = 'https://steamcommunity.com/profiles/76561199488729915/'
    
        weblist = [Telegram, YouTube, Discord, Steam]
        try:
            for i in weblist:
                WEB.open_new_tab(i)
        except:
            pass

    