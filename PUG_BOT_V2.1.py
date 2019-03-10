import discord
from discord.ext import commands
import random
import datetime
import asyncio

description = 'A pug bot for Overwatch Israel.'
bot = commands.Bot(command_prefix='!', description=description)

token = ''

client = discord.client


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='twitch.tv/ow_il'))
    print('Fired up!')


@bot.command()
async def pug(ctx):
    """ make an async def (roles) and run it inside every choice just above the member_list.remove """
    Bronze = discord.utils.get(ctx.guild.roles, name="Bronze")
    print(type(Bronze))
    voice_channel = discord.utils.get(ctx.guild.channels, id=542042691811409973)
    team_1_vc = discord.utils.get(ctx.guild.channels, id=546297542158057492)
    team_2_vc = discord.utils.get(ctx.guild.channels, id=546337215911952384)
    member_list1 = voice_channel.members
    Pug_Runner = discord.utils.get(ctx.guild.roles, name="PUG Runner")

    list_of_forced_players = []
    """
    if len(member_list1) < 12:
        message = await ctx.send('Not enough members to start a PUG.')
        await asyncio.sleep(10)
        await message.delete()
    """
    while len(member_list1) > 12:
        choice = random.choice(member_list1)
        if choice not in list_of_forced_players:
            list_of_forced_players = list_of_forced_players + [choice.mention]
            member_list1.remove(choice)

    if len(member_list1) <= 12:
        if Pug_Runner in ctx.author.roles:
            async def startup(difference):
                voice_channel = discord.utils.get(ctx.guild.channels, id=542042691811409973)
                team_1_vc = discord.utils.get(ctx.guild.channels, id=546297542158057492)
                team_2_vc = discord.utils.get(ctx.guild.channels, id=546337215911952384)
                Main_DPS = discord.utils.get(ctx.guild.roles, name="DPS")
                DPS = discord.utils.get(ctx.guild.roles, name="Secondary - DPS")
                Tank = discord.utils.get(ctx.guild.roles, name="Secondary - Tank")
                Main_Tank = discord.utils.get(ctx.guild.roles, name="Tank")
                Main_Support = discord.utils.get(ctx.guild.roles, name="Support")
                Support = discord.utils.get(ctx.guild.roles, name="Secondary - Support")
                Bronze = discord.utils.get(ctx.guild.roles, name="Bronze")
                Silver = discord.utils.get(ctx.guild.roles, name="Silver")
                Gold = discord.utils.get(ctx.guild.roles, name="Gold")
                Platinum = discord.utils.get(ctx.guild.roles, name="Platinum")
                Diamond = discord.utils.get(ctx.guild.roles, name="Diamond")
                Master = discord.utils.get(ctx.guild.roles, name="Master")
                Grandmaster = discord.utils.get(ctx.guild.roles, name="Grandmaster")
                Top500 = discord.utils.get(ctx.guild.roles, name="Top 500")
                member_list = member_list1
                important_list_swear_to_god = "[<Member id=206955935229280256 name='Senpai' discriminator='4451' bot=True nick='%' guild=<Guild id=542042691811409961 name='bot_testing' chunked=True>>, <Member id=234395307759108106 name='Groovy' discriminator='7254' bot=True nick='-' guild=<Guild id=542042691811409961 name='bot_testing' chunked=True>>, <Member id=235088799074484224 name='Rythm' discriminator='3722' bot=True nick='!' guild=<Guild id=542042691811409961 name='bot_testing' chunked=True>>, <Member id=239631525350604801 name='Pancake' discriminator='3691' bot=True nick='p!' guild=<Guild id=542042691811409961 name='bot_testing' chunked=True>>, <Member id=247134460024193027 name='Strodl Bot' discriminator='6741' bot=True nick='&' guild=<Guild id=542042691811409961 name='bot_testing' chunked=True>>, <Member id=251930037673132032 name='Mewna' discriminator='2576' bot=True nick='mew.' guild=<Guild id=542042691811409961 name='bot_testing' chunked=True>>, <Member id=284035252408680448 name='Tony Bamanaboni XD' discriminator='3926' bot=True nick='%' guild=<Guild id=542042691811409961 name='bot_testing' chunked=True>>, <Member id=303181184718995457 name='PenguBot' discriminator='9722' bot=True nick='p!' guild=<Guild id=542042691811409961 name='bot_testing' chunked=True>>, <Member id=308528241616879617 name='Anyatsu' discriminator='6395' bot=False nick=None guild=<Guild id=542042691811409961 name='bot_testing' chunked=True>>, <Member id=318461955448766474 name='sPOONY' discriminator='2958' bot=False nick=None guild=<Guild id=542042691811409961 name='bot_testing' chunked=True>>, <Member id=346577085155901451 name='TomBot' discriminator='6419' bot=True nick='>' guild=<Guild id=542042691811409961 name='bot_testing' chunked=True>>, <Member id=469610550159212554 name='ZeroTwo' discriminator='3859' bot=True nick='zt!' guild=<Guild id=542042691811409961 name='bot_testing' chunked=True>>]"

                choice1 = discord.Member
                choice2 = discord.Member
                choice3 = discord.Member
                choice4 = discord.Member
                choice5 = discord.Member
                choice6 = discord.Member
                choice7 = discord.Member
                choice8 = discord.Member
                choice9 = discord.Member
                choice10 = discord.Member
                choice11 = discord.Member
                choice12 = discord.Member
                list_of_supports = []
                team_1_supports = []
                team_2_supports = []
                team_1_sr = 0
                team_2_sr = 0

                def numbers(member, team_1_sr):
                    if Bronze in member.roles:
                        team_1_sr = team_1_sr + 1000
                    elif Silver in member.roles:
                        team_1_sr = team_1_sr + 1500
                    elif Gold in member.roles:
                        team_1_sr = team_1_sr + 2000
                    elif Platinum in member.roles:
                        team_1_sr = team_1_sr + 2500
                    elif Diamond in member.roles:
                        team_1_sr = team_1_sr + 3000
                    elif Master in member.roles:
                        team_1_sr = team_1_sr + 3500
                    elif Grandmaster in member.roles:
                        team_1_sr = team_1_sr + 4000
                    elif Top500 in member.roles:
                        team_1_sr = team_1_sr + 4200
                    team_1_sr = team_1_sr


                for member in member_list:
                    if Main_Support in member.roles:
                        list_of_supports = list_of_supports + [member]

                while len(list_of_supports) > 4:
                    choice = random.choice(list_of_supports)
                    list_of_supports.remove(choice)

                if len(list_of_supports) == 4:
                    choice1 = random.choice(list_of_supports)
                    team_1_supports = team_1_supports + [choice1.mention]
                    member_list.remove(choice1)
                    list_of_supports.remove(choice1)
                    if Bronze in choice1.roles:
                        team_1_sr = team_1_sr + 1000
                    elif Silver in choice1.roles:
                        team_1_sr = team_1_sr + 1500
                    elif Gold in choice1.roles:
                        team_1_sr = team_1_sr + 2000
                    elif Platinum in choice1.roles:
                        team_1_sr = team_1_sr + 2500
                    elif Diamond in choice1.roles:
                        team_1_sr = team_1_sr + 3000
                    elif Master in choice1.roles:
                        team_1_sr = team_1_sr + 3500
                    elif Grandmaster in choice1.roles:
                        team_1_sr = team_1_sr + 4000
                    elif Top500 in choice1.roles:
                        team_1_sr = team_1_sr + 4200

                    choice2 = random.choice(list_of_supports)
                    team_1_supports = team_1_supports + [choice2.mention]
                    member_list.remove(choice2)
                    list_of_supports.remove(choice2)

                    if Bronze in choice2.roles:
                        team_1_sr = team_1_sr + 1000
                    elif Silver in choice2.roles:
                        team_1_sr = team_1_sr + 1500
                    elif Gold in choice2.roles:
                        team_1_sr = team_1_sr + 2000
                    elif Platinum in choice2.roles:
                        team_1_sr = team_1_sr + 2500
                    elif Diamond in choice2.roles:
                        team_1_sr = team_1_sr + 3000
                    elif Master in choice2.roles:
                        team_1_sr = team_1_sr + 3500
                    elif Grandmaster in choice2.roles:
                        team_1_sr = team_1_sr + 4000
                    elif Top500 in choice2.roles:
                        team_1_sr = team_1_sr + 4200

                    choice3 = random.choice(list_of_supports)
                    team_2_supports = team_2_supports + [choice3.mention]
                    member_list.remove(choice3)
                    list_of_supports.remove(choice3)
                    if Bronze in choice3.roles:
                        team_2_sr = team_2_sr + 1000
                    elif Silver in choice3.roles:
                        team_2_sr = team_2_sr + 1500
                    elif Gold in choice3.roles:
                        team_2_sr = team_2_sr + 2000
                    elif Platinum in choice3.roles:
                        team_2_sr = team_2_sr + 2500
                    elif Diamond in choice3.roles:
                        team_2_sr = team_2_sr + 3000
                    elif Master in choice3.roles:
                        team_2_sr = team_2_sr + 3500
                    elif Grandmaster in choice3.roles:
                        team_2_sr = team_2_sr + 4000
                    elif Top500 in choice3.roles:
                        team_2_sr = team_2_sr + 4200

                    choice4 = random.choice(list_of_supports)
                    team_2_supports = team_2_supports + [choice4.mention]
                    member_list.remove(choice4)
                    list_of_supports.remove(choice4)
                    if Bronze in choice4.roles:
                        team_2_sr = team_2_sr + 1000
                    elif Silver in choice4.roles:
                        team_2_sr = team_2_sr + 1500
                    elif Gold in choice4.roles:
                        team_2_sr = team_2_sr + 2000
                    elif Platinum in choice4.roles:
                        team_2_sr = team_2_sr + 2500
                    elif Diamond in choice4.roles:
                        team_2_sr = team_2_sr + 3000
                    elif Master in choice4.roles:
                        team_2_sr = team_2_sr + 3500
                    elif Grandmaster in choice4.roles:
                        team_2_sr = team_2_sr + 4000
                    elif Top500 in choice4.roles:
                        team_2_sr = team_2_sr + 4200

                elif len(list_of_supports) < 4:
                    for member in member_list:
                        if Support in member.roles:
                            list_of_supports = list_of_supports + [member]
                    if len(list_of_supports) == 4:
                        choice1 = random.choice(list_of_supports)
                        team_1_supports = team_1_supports + [choice1.mention]
                        member_list.remove(choice1)
                        list_of_supports.remove(choice1)
                        if Bronze in choice1.roles:
                            team_1_sr = team_1_sr + 1000
                        elif Silver in choice1.roles:
                            team_1_sr = team_1_sr + 1500
                        elif Gold in choice1.roles:
                            team_1_sr = team_1_sr + 2000
                        elif Platinum in choice1.roles:
                            team_1_sr = team_1_sr + 2500
                        elif Diamond in choice1.roles:
                            team_1_sr = team_1_sr + 3000
                        elif Master in choice1.roles:
                            team_1_sr = team_1_sr + 3500
                        elif Grandmaster in choice1.roles:
                            team_1_sr = team_1_sr + 4000
                        elif Top500 in choice1.roles:
                            team_1_sr = team_1_sr + 4200

                        choice2 = random.choice(list_of_supports)
                        team_1_supports = team_1_supports + [choice2.mention]
                        member_list.remove(choice2)
                        list_of_supports.remove(choice2)

                        if Bronze in choice2.roles:
                            team_1_sr = team_1_sr + 1000
                        elif Silver in choice2.roles:
                            team_1_sr = team_1_sr + 1500
                        elif Gold in choice2.roles:
                            team_1_sr = team_1_sr + 2000
                        elif Platinum in choice2.roles:
                            team_1_sr = team_1_sr + 2500
                        elif Diamond in choice2.roles:
                            team_1_sr = team_1_sr + 3000
                        elif Master in choice2.roles:
                            team_1_sr = team_1_sr + 3500
                        elif Grandmaster in choice2.roles:
                            team_1_sr = team_1_sr + 4000
                        elif Top500 in choice2.roles:
                            team_1_sr = team_1_sr + 4200

                        choice3 = random.choice(list_of_supports)
                        team_2_supports = team_2_supports + [choice3.mention]
                        member_list.remove(choice3)
                        list_of_supports.remove(choice3)
                        if Bronze in choice3.roles:
                            team_2_sr = team_2_sr + 1000
                        elif Silver in choice3.roles:
                            team_2_sr = team_2_sr + 1500
                        elif Gold in choice3.roles:
                            team_2_sr = team_2_sr + 2000
                        elif Platinum in choice3.roles:
                            team_2_sr = team_2_sr + 2500
                        elif Diamond in choice3.roles:
                            team_2_sr = team_2_sr + 3000
                        elif Master in choice3.roles:
                            team_2_sr = team_2_sr + 3500
                        elif Grandmaster in choice3.roles:
                            team_2_sr = team_2_sr + 4000
                        elif Top500 in choice3.roles:
                            team_2_sr = team_2_sr + 4200

                        choice4 = random.choice(list_of_supports)
                        team_2_supports = team_2_supports + [choice4.mention]
                        member_list.remove(choice4)
                        list_of_supports.remove(choice4)
                        if Bronze in choice4.roles:
                            team_2_sr = team_2_sr + 1000
                        elif Silver in choice4.roles:
                            team_2_sr = team_2_sr + 1500
                        elif Gold in choice4.roles:
                            team_2_sr = team_2_sr + 2000
                        elif Platinum in choice4.roles:
                            team_2_sr = team_2_sr + 2500
                        elif Diamond in choice4.roles:
                            team_2_sr = team_2_sr + 3000
                        elif Master in choice4.roles:
                            team_2_sr = team_2_sr + 3500
                        elif Grandmaster in choice4.roles:
                            team_2_sr = team_2_sr + 4000
                        elif Top500 in choice4.roles:
                            team_2_sr = team_2_sr + 4200

                    while len(list_of_supports) > 4:
                        choice = random.choice(list_of_supports)
                        if Main_Support not in choice.roles:
                            list_of_supports.remove(choice)

                    if len(list_of_supports) == 3:
                        choice = random.choice(member_list)
                        print(len(list_of_supports))
                        list_of_supports = list_of_supports + [choice]

                    elif len(list_of_supports) == 2:
                        choice = random.choice(member_list)
                        print(len(list_of_supports))
                        list_of_supports = list_of_supports + [choice]
                        choice = random.choice(member_list)
                        print(len(list_of_supports))
                        list_of_supports = list_of_supports + [choice]

                list_of_tanks = []
                team_1_tanks = []
                team_2_tanks = []

                for member in member_list:
                    if Main_Tank in member.roles:
                        list_of_tanks = list_of_tanks + [member]
                if len(list_of_tanks) < 4:  # what to do if there are less then 4 maintanks
                    for member in member_list:
                        if Tank in member.roles:
                            list_of_tanks = list_of_tanks + [member]

                    if len(list_of_tanks) == 3:
                        choice = random.choice(member_list)
                        print(len(list_of_tanks))
                        list_of_tanks = list_of_tanks + [choice]

                    if len(list_of_tanks) == 2:
                        choice = random.choice(member_list)
                        print(len(list_of_tanks))
                        list_of_tanks = list_of_tanks + [choice]
                        choice = random.choice(member_list)
                        print(len(list_of_tanks))
                        list_of_tanks = list_of_tanks + [choice]

                    if len(list_of_tanks) == 4:
                        choice5 = random.choice(list_of_tanks)
                        team_1_tanks = team_1_tanks + [choice5.mention]
                        list_of_tanks.remove(choice5)
                        member_list.remove(choice5)
                        if Bronze in choice5.roles:
                            team_1_sr = team_1_sr + 1000
                        elif Silver in choice5.roles:
                            team_1_sr = team_1_sr + 1500
                        elif Gold in choice5.roles:
                            team_1_sr = team_1_sr + 2000
                        elif Platinum in choice5.roles:
                            team_1_sr = team_1_sr + 2500
                        elif Diamond in choice5.roles:
                            team_1_sr = team_1_sr + 3000
                        elif Master in choice5.roles:
                            team_1_sr = team_1_sr + 3500
                        elif Grandmaster in choice5.roles:
                            team_1_sr = team_1_sr + 4000
                        elif Top500 in choice5.roles:
                            team_1_sr = team_1_sr + 4200

                        choice6 = random.choice(list_of_tanks)
                        team_1_tanks = team_1_tanks + [choice6.mention]
                        list_of_tanks.remove(choice6)
                        member_list.remove(choice6)
                        if Bronze in choice6.roles:
                            team_1_sr = team_1_sr + 1000
                        elif Silver in choice6.roles:
                            team_1_sr = team_1_sr + 1500
                        elif Gold in choice6.roles:
                            team_1_sr = team_1_sr + 2000
                        elif Platinum in choice6.roles:
                            team_1_sr = team_1_sr + 2500
                        elif Diamond in choice6.roles:
                            team_1_sr = team_1_sr + 3000
                        elif Master in choice6.roles:
                            team_1_sr = team_1_sr + 3500
                        elif Grandmaster in choice6.roles:
                            team_1_sr = team_1_sr + 4000
                        elif Top500 in choice6.roles:
                            team_1_sr = team_1_sr + 4200

                        choice7 = random.choice(list_of_tanks)
                        team_2_tanks = team_2_tanks + [choice7.mention]
                        list_of_tanks.remove(choice7)
                        member_list.remove(choice7)
                        if Bronze in choice7.roles:
                            team_2_sr = team_2_sr + 1000
                        elif Silver in choice7.roles:
                            team_2_sr = team_2_sr + 1500
                        elif Gold in choice7.roles:
                            team_2_sr = team_2_sr + 2000
                        elif Platinum in choice7.roles:
                            team_2_sr = team_2_sr + 2500
                        elif Diamond in choice7.roles:
                            team_2_sr = team_2_sr + 3000
                        elif Master in choice7.roles:
                            team_2_sr = team_2_sr + 3500
                        elif Grandmaster in choice7.roles:
                            team_2_sr = team_2_sr + 4000
                        elif Top500 in choice7.roles:
                            team_2_sr = team_2_sr + 4200

                        choice8 = random.choice(list_of_tanks)
                        team_2_tanks = team_2_tanks + [choice8.mention]
                        list_of_tanks.remove(choice8)
                        member_list.remove(choice8)
                        if Bronze in choice8.roles:
                            team_2_sr = team_2_sr + 1000
                        elif Silver in choice8.roles:
                            team_2_sr = team_2_sr + 1500
                        elif Gold in choice8.roles:
                            team_2_sr = team_2_sr + 2000
                        elif Platinum in choice8.roles:
                            team_2_sr = team_2_sr + 2500
                        elif Diamond in choice8.roles:
                            team_2_sr = team_2_sr + 3000
                        elif Master in choice8.roles:
                            team_2_sr = team_2_sr + 3500
                        elif Grandmaster in choice8.roles:
                            team_2_sr = team_2_sr + 4000
                        elif Top500 in choice8.roles:
                            team_2_sr = team_2_sr + 4200

                    while len(list_of_tanks) > 4:
                        choice1 = random.choice(list_of_tanks)
                        if Tank in choice1.roles:
                            list_of_tanks.remove(choice1)

                while len(list_of_tanks) > 4:
                    choice1 = random.choice(list_of_tanks)
                    list_of_tanks.remove(choice1)

                if len(list_of_tanks) == 4:
                    choice5 = random.choice(list_of_tanks)
                    team_1_tanks = team_1_tanks + [choice5.mention]
                    list_of_tanks.remove(choice5)
                    member_list.remove(choice5)
                    if Bronze in choice5.roles:
                        team_1_sr = team_1_sr + 1000
                    elif Silver in choice5.roles:
                        team_1_sr = team_1_sr + 1500
                    elif Gold in choice5.roles:
                        team_1_sr = team_1_sr + 2000
                    elif Platinum in choice5.roles:
                        team_1_sr = team_1_sr + 2500
                    elif Diamond in choice5.roles:
                        team_1_sr = team_1_sr + 3000
                    elif Master in choice5.roles:
                        team_1_sr = team_1_sr + 3500
                    elif Grandmaster in choice5.roles:
                        team_1_sr = team_1_sr + 4000
                    elif Top500 in choice5.roles:
                        team_1_sr = team_1_sr + 4200

                    choice6 = random.choice(list_of_tanks)
                    team_1_tanks = team_1_tanks + [choice6.mention]
                    list_of_tanks.remove(choice6)
                    member_list.remove(choice6)
                    if Bronze in choice6.roles:
                        team_1_sr = team_1_sr + 1000
                    elif Silver in choice6.roles:
                        team_1_sr = team_1_sr + 1500
                    elif Gold in choice6.roles:
                        team_1_sr = team_1_sr + 2000
                    elif Platinum in choice6.roles:
                        team_1_sr = team_1_sr + 2500
                    elif Diamond in choice6.roles:
                        team_1_sr = team_1_sr + 3000
                    elif Master in choice6.roles:
                        team_1_sr = team_1_sr + 3500
                    elif Grandmaster in choice6.roles:
                        team_1_sr = team_1_sr + 4000
                    elif Top500 in choice6.roles:
                        team_1_sr = team_1_sr + 4200

                    choice7 = random.choice(list_of_tanks)
                    team_2_tanks = team_2_tanks + [choice7.mention]
                    list_of_tanks.remove(choice7)
                    member_list.remove(choice7)
                    if Bronze in choice7.roles:
                        team_2_sr = team_2_sr + 1000
                    elif Silver in choice7.roles:
                        team_2_sr = team_2_sr + 1500
                    elif Gold in choice7.roles:
                        team_2_sr = team_2_sr + 2000
                    elif Platinum in choice7.roles:
                        team_2_sr = team_2_sr + 2500
                    elif Diamond in choice7.roles:
                        team_2_sr = team_2_sr + 3000
                    elif Master in choice7.roles:
                        team_2_sr = team_2_sr + 3500
                    elif Grandmaster in choice7.roles:
                        team_2_sr = team_2_sr + 4000
                    elif Top500 in choice7.roles:
                        team_2_sr = team_2_sr + 4200

                    choice8 = random.choice(list_of_tanks)
                    team_2_tanks = team_2_tanks + [choice8.mention]
                    list_of_tanks.remove(choice8)
                    member_list.remove(choice8)
                    if Bronze in choice8.roles:
                        team_2_sr = team_2_sr + 1000
                    elif Silver in choice8.roles:
                        team_2_sr = team_2_sr + 1500
                    elif Gold in choice8.roles:
                        team_2_sr = team_2_sr + 2000
                    elif Platinum in choice8.roles:
                        team_2_sr = team_2_sr + 2500
                    elif Diamond in choice8.roles:
                        team_2_sr = team_2_sr + 3000
                    elif Master in choice8.roles:
                        team_2_sr = team_2_sr + 3500
                    elif Grandmaster in choice8.roles:
                        team_2_sr = team_2_sr + 4000
                    elif Top500 in choice8.roles:
                        team_2_sr = team_2_sr + 4200

                list_of_dps = []
                team_1_dps = []
                team_2_dps = []

                for member in member_list:
                    if Main_DPS in member.roles:
                        list_of_dps = list_of_dps + [member]

                while len(list_of_dps) > 4:
                    choice = random.choice(list_of_dps)
                    if DPS or Main_DPS not in choice.roles:
                        list_of_dps.remove(choice)

                if len(list_of_dps) == 4:
                    choice9 = random.choice(list_of_dps)
                    team_1_dps = team_1_dps + [choice9.mention]
                    list_of_dps.remove(choice9)
                    if Bronze in choice9.roles:
                        team_1_sr = team_1_sr + 1000
                    elif Silver in choice9.roles:
                        team_1_sr = team_1_sr + 1500
                    elif Gold in choice9.roles:
                        team_1_sr = team_1_sr + 2000
                    elif Platinum in choice9.roles:
                        team_1_sr = team_1_sr + 2500
                    elif Diamond in choice9.roles:
                        team_1_sr = team_1_sr + 3000
                    elif Master in choice9.roles:
                        team_1_sr = team_1_sr + 3500
                    elif Grandmaster in choice9.roles:
                        team_1_sr = team_1_sr + 4000
                    elif Top500 in choice9.roles:
                        team_1_sr = team_1_sr + 4200

                    choice10 = random.choice(list_of_dps)
                    team_1_dps = team_1_dps + [choice10.mention]
                    list_of_dps.remove(choice10)
                    if Bronze in choice10.roles:
                        team_1_sr = team_1_sr + 1000
                    elif Silver in choice10.roles:
                        team_1_sr = team_1_sr + 1500
                    elif Gold in choice10.roles:
                        team_1_sr = team_1_sr + 2000
                    elif Platinum in choice10.roles:
                        team_1_sr = team_1_sr + 2500
                    elif Diamond in choice10.roles:
                        team_1_sr = team_1_sr + 3000
                    elif Master in choice10.roles:
                        team_1_sr = team_1_sr + 3500
                    elif Grandmaster in choice10.roles:
                        team_1_sr = team_1_sr + 4000
                    elif Top500 in choice10.roles:
                        team_1_sr = team_1_sr + 4200

                    choice11 = random.choice(list_of_dps)
                    team_2_dps = team_2_dps + [choice11.mention]
                    list_of_dps.remove(choice11)
                    if Bronze in choice11.roles:
                        team_2_sr = team_2_sr + 1000
                    elif Silver in choice11.roles:
                        team_2_sr = team_2_sr + 1500
                    elif Gold in choice11.roles:
                        team_2_sr = team_2_sr + 2000
                    elif Platinum in choice11.roles:
                        team_2_sr = team_2_sr + 2500
                    elif Diamond in choice11.roles:
                        team_2_sr = team_2_sr + 3000
                    elif Master in choice11.roles:
                        team_2_sr = team_2_sr + 3500
                    elif Grandmaster in choice11.roles:
                        team_2_sr = team_2_sr + 4000
                    elif Top500 in choice11.roles:
                        team_2_sr = team_2_sr + 4200

                    choice12 = random.choice(list_of_dps)
                    team_2_dps = team_2_dps + [choice12.mention]
                    list_of_dps.remove(choice12)
                    if Bronze in choice12.roles:
                        team_2_sr = team_2_sr + 1000
                    elif Silver in choice12.roles:
                        team_2_sr = team_2_sr + 1500
                    elif Gold in choice12.roles:
                        team_2_sr = team_2_sr + 2000
                    elif Platinum in choice12.roles:
                        team_2_sr = team_2_sr + 2500
                    elif Diamond in choice12.roles:
                        team_2_sr = team_2_sr + 3000
                    elif Master in choice12.roles:
                        team_2_sr = team_2_sr + 3500
                    elif Grandmaster in choice12.roles:
                        team_2_sr = team_2_sr + 4000
                    elif Top500 in choice12.roles:
                        team_2_sr = team_2_sr + 4200

                if len(list_of_dps) < 4:
                    for member in member_list:
                        if DPS in member.roles:
                            list_of_dps = list_of_dps + [member]

                    if len(list_of_dps) < 4:
                        list_of_dps = member_list

                    if len(list_of_dps) > 4:
                        choice = random.choice(list_of_dps)
                        if DPS in choice.roles:
                            list_of_dps.remove(choice)

                    if len(list_of_dps) == 4:
                        choice9 = random.choice(list_of_dps)
                        team_1_dps = team_1_dps + [choice9.mention]
                        list_of_dps.remove(choice9)
                        if Bronze in choice9.roles:
                            team_1_sr = team_1_sr + 1000
                        elif Silver in choice9.roles:
                            team_1_sr = team_1_sr + 1500
                        elif Gold in choice9.roles:
                            team_1_sr = team_1_sr + 2000
                        elif Platinum in choice9.roles:
                            team_1_sr = team_1_sr + 2500
                        elif Diamond in choice9.roles:
                            team_1_sr = team_1_sr + 3000
                        elif Master in choice9.roles:
                            team_1_sr = team_1_sr + 3500
                        elif Grandmaster in choice9.roles:
                            team_1_sr = team_1_sr + 4000
                        elif Top500 in choice9.roles:
                            team_1_sr = team_1_sr + 4200

                        choice10 = random.choice(list_of_dps)
                        team_1_dps = team_1_dps + [choice10.mention]
                        list_of_dps.remove(choice10)
                        if Bronze in choice10.roles:
                            team_1_sr = team_1_sr + 1000
                        elif Silver in choice10.roles:
                            team_1_sr = team_1_sr + 1500
                        elif Gold in choice10.roles:
                            team_1_sr = team_1_sr + 2000
                        elif Platinum in choice10.roles:
                            team_1_sr = team_1_sr + 2500
                        elif Diamond in choice10.roles:
                            team_1_sr = team_1_sr + 3000
                        elif Master in choice10.roles:
                            team_1_sr = team_1_sr + 3500
                        elif Grandmaster in choice10.roles:
                            team_1_sr = team_1_sr + 4000
                        elif Top500 in choice10.roles:
                            team_1_sr = team_1_sr + 4200

                        choice11 = random.choice(list_of_dps)
                        team_2_dps = team_2_dps + [choice11.mention]
                        list_of_dps.remove(choice11)
                        if Bronze in choice11.roles:
                            team_2_sr = team_2_sr + 1000
                        elif Silver in choice11.roles:
                            team_2_sr = team_2_sr + 1500
                        elif Gold in choice11.roles:
                            team_2_sr = team_2_sr + 2000
                        elif Platinum in choice11.roles:
                            team_2_sr = team_2_sr + 2500
                        elif Diamond in choice11.roles:
                            team_2_sr = team_2_sr + 3000
                        elif Master in choice11.roles:
                            team_2_sr = team_2_sr + 3500
                        elif Grandmaster in choice11.roles:
                            team_2_sr = team_2_sr + 4000
                        elif Top500 in choice11.roles:
                            team_2_sr = team_2_sr + 4200

                        choice12 = random.choice(list_of_dps)
                        team_2_dps = team_2_dps + [choice12.mention]
                        list_of_dps.remove(choice12)
                        if Bronze in choice12.roles:
                            team_2_sr = team_2_sr + 1000
                        elif Silver in choice12.roles:
                            team_2_sr = team_2_sr + 1500
                        elif Gold in choice12.roles:
                            team_2_sr = team_2_sr + 2000
                        elif Platinum in choice12.roles:
                            team_2_sr = team_2_sr + 2500
                        elif Diamond in choice12.roles:
                            team_2_sr = team_2_sr + 3000
                        elif Master in choice12.roles:
                            team_2_sr = team_2_sr + 3500
                        elif Grandmaster in choice12.roles:
                            team_2_sr = team_2_sr + 4000
                        elif Top500 in choice12.roles:
                            team_2_sr = team_2_sr + 420

                print(team_1_sr, team_2_sr)

                embed2 = discord.Embed(
                    title='These players did not get picked this time, but they will play in the next game: ',
                    description=str(list_of_forced_players), colour=discord.Colour.dark_orange()
                )
                embed = discord.Embed(
                    title='**__Team 1:__**',
                    colour=discord.Colour.dark_blue()
                )
                embed.set_footer(
                    text='Coded by sPOONY#2958 | ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                embed.add_field(name='Supports: ', value=str(team_1_supports), inline=False)
                embed.add_field(name='Tanks:', value=str(team_1_tanks), inline=False)
                embed.add_field(name='DPS:', value=str(team_1_dps), inline=False)
                embed1 = discord.Embed(
                    title='**__Team 2:__**', colour=discord.Colour.dark_red()
                )
                embed1.set_footer(
                    text='Coded by sPOONY#2958 | ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                embed1.add_field(name='Supports: ', value=str(team_2_supports), inline=False)
                embed1.add_field(name='Tanks:', value=str(team_2_tanks), inline=False)
                embed1.add_field(name='DPS:', value=str(team_2_dps), inline=False)
                # embed1.add_field(name='SR Difference:', value=str(difference))
                await ctx.send(embed=embed)
                await ctx.send(embed=embed1)

            await startup(250)
        else:
            message = await ctx.send("You're not a PUG Runner!")
            await asyncio.sleep(10)
            await message.delete()


"""@bot.command()
async def test(ctx):
    team_1_supports = 'a'
    team_1_tanks = 'b'
    team_1_dps = 'c'
    team_2_supports = 'd'
    team_2_tanks = 'e'
    team_2_dps = 'f'
    list_of_forced_players = 'y'

    embed = discord.Embed(
        title='**__Team 1:__**',
        colour=discord.Colour.dark_blue()
    )
    embed.set_footer(
        text='Coded by sPOONY#2958 | ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    embed.add_field(name='Supports: ', value=str(team_1_supports), inline=False)
    embed.add_field(name='Tanks:', value=str(team_1_tanks), inline=False)
    embed.add_field(name='DPS:', value=str(team_1_dps), inline=False)
    embed1 = discord.Embed(
        title='**__Team 2:__**', colour=discord.Colour.dark_red()
    )
    embed1.set_footer(text='Coded by sPOONY#2958 | ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    embed1.add_field(name='Supports: ', value=str(team_2_supports), inline=False)
    embed1.add_field(name='Tanks:', value=str(team_2_tanks), inline=False)
    embed1.add_field(name='DPS:', value=str(team_2_dps), inline=False)
    if list_of_forced_players != []:
        embed2 = discord.Embed(
            title='These players did not get picked this time, but they will play in the next game: ',
            description=str(list_of_forced_players), colour=discord.Colour.dark_orange()
        )
    await ctx.send(embed=embed)
    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)
"""
@bot.command()
async def move(ctx):
    team_1_vc = discord.utils.get(ctx.guild.channels, id=505023848425455616)
    team_2_vc = discord.utils.get(ctx.guild.channels, id=505023650202648577)
    voice_channel = discord.utils.get(ctx.guild.channels, id=547108815435464717)
    list_of_members_t1 = team_1_vc.members
    list_of_members_t2 = team_2_vc.members
    while len(list_of_members_t1) != 0:
            choice1 = random.choice(list_of_members_t1)
            await choice1.move_to(voice_channel)
            list_of_members_t1.remove(choice1)
    while len(list_of_members_t2) != 0:
        choice1 = random.choice(list_of_members_t2)
        await choice1.move_to(voice_channel)
        list_of_members_t2.remove(choice1)
    print('all donezo!')


bot.run(token)
