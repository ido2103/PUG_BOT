import discord
from discord.ext import commands
from discord.utils import get
import random
import datetime

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
    Main_DPS = discord.utils.get(ctx.guild.roles, name="DPS")
    DPS = discord.utils.get(ctx.guild.roles, name="Secondary - DPS")
    Tank = discord.utils.get(ctx.guild.roles, name="Secondary - Tank")
    Main_Tank = discord.utils.get(ctx.guild.roles, name="Tank")
    Main_Support = discord.utils.get(ctx.guild.roles, name="Support")
    Support = discord.utils.get(ctx.guild.roles, name="Secondary - Support")
    Pug_Runner = discord.utils.get(ctx.guild.roles, name="PUG Runner")

    list_of_forced_players = []
    number_of_forced_players = int
    voice_channel = discord.utils.get(ctx.guild.channels, id=542042691811409973)
    team_1_vc = discord.utils.get(ctx.guild.channels, id=546297542158057492)
    team_2_vc = discord.utils.get(ctx.guild.channels, id=546337215911952384)
    member_list = voice_channel.members
    choice1 = discord.Member
    choice2 = discord.Member
    choice3 = discord.Member
    choice4 = discord.Member

    if len(member_list) < 12:
        # what to do if there are less then 12 people in the vc
        await ctx.send('Not enough members to start a PUG')

    while len(member_list) > 12:
        # what to do if there are more then 12 people in the vc - the force players system
        choice = random.choice(member_list)
        if choice not in list_of_forced_players:
            list_of_forced_players = list_of_forced_players + [choice.mention]
            member_list.remove(choice)

    if len(member_list) == 12:
        # if there are only 12 people - no forced players
        if Pug_Runner in ctx.author.roles:

            list_of_supports = []
            team_1_supports = []
            team_2_supports = []
            list_of_supports_fillers = []

            for member in member_list:
                if Main_Support in member.roles:
                    list_of_supports = list_of_supports + [member]

            if len(list_of_supports) < 4:  # what to do if there are less then 4 maintanks
                for member in member_list:
                    if Support in member.roles:
                        list_of_supports = list_of_supports + [member]

                if len(list_of_supports) < 4:
                    number1 = len(list_of_supports)
                    number = 4 - number1
                    print(number1)
                    print(number)
                    list_of_fillers = []
                    while number != 0:
                        for member in member_list:
                            if DPS or Main_DPS or Tank or Main_Tank in member.roles:
                                list_of_fillers = list_of_fillers + [member]
                        choice = random.choice(list_of_fillers)
                        list_of_supports = list_of_supports + [choice]
                        number -= 1
                        print(number)

                if len(list_of_supports) == 4:
                    choice1 = random.choice(list_of_supports)
                    team_1_supports = team_1_supports + [choice1]
                    await choice1.send("You're playing **SUPPORT** for **TEAM 1**. The PUG took place in: " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    await choice1.move_to(team_1_vc)
                    list_of_supports.remove(choice1)
                    member_list.remove(choice1)
                    choice2 = random.choice(list_of_supports)
                    team_1_supports = team_1_supports + [choice2]
                    await choice2.send("You're playing **SUPPORT** for **TEAM 1**. The PUG took place in: " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    await choice2.move_to(team_1_vc)
                    list_of_supports.remove(choice2)
                    member_list.remove(choice2)
                    choice3 = random.choice(list_of_supports)
                    team_2_supports = team_2_supports + [choice3]
                    await choice3.send("You're playing **SUPPORT** for **TEAM 2**. The PUG took place in: " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    await choice3.move_to(team_2_vc)
                    list_of_supports.remove(choice3)
                    member_list.remove(choice3)
                    choice4 = random.choice(list_of_supports)
                    team_2_supports = team_2_supports + [choice4]
                    await choice4.send("You're playing **SUPPORT** for **TEAM 2**. The PUG took place in: " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

                    await choice4.move_to(team_2_vc)
                    list_of_supports.remove(choice4)
                    member_list.remove(choice4)

                while len(list_of_supports) > 4:
                    choice1 = random.choice(list_of_supports)
                    if Support in choice1.roles:
                        list_of_supports.remove(choice1)

            while len(list_of_supports) >= 5:
                choice1 = random.choice(list_of_supports)
                list_of_supports.remove(choice1)

            if len(list_of_supports) == 4:
                choice1 = random.choice(list_of_supports)
                team_1_supports = team_1_supports + [choice1.mention]
                await choice1.send("You're playing **SUPPORT** for **TEAM 1**. The PUG took place in: " + str(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

                await choice1.move_to(team_1_vc)
                list_of_supports.remove(choice1)
                member_list.remove(choice1)
                choice2 = random.choice(list_of_supports)
                team_1_supports = team_1_supports + [choice2.mention]
                await choice2.send("You're playing **SUPPORT** for **TEAM 1**. The PUG took place in: " + str(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

                await choice2.move_to(team_1_vc)
                list_of_supports.remove(choice2)
                member_list.remove(choice2)
                choice3 = random.choice(list_of_supports)
                team_2_supports = team_2_supports + [choice3.mention]
                await choice3.send("You're playing **SUPPORT** for **TEAM 2**. The PUG took place in: " + str(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

                await choice3.move_to(team_2_vc)
                list_of_supports.remove(choice3)
                member_list.remove(choice3)
                choice4 = random.choice(list_of_supports)
                team_2_supports = team_2_supports + [choice4.mention]
                await choice4.send("You're playing **SUPPORT** for **TEAM 2**. The PUG took place in: " + str(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                await choice4.move_to(team_2_vc)
                list_of_supports.remove(choice4)
                member_list.remove(choice4)

                # -----------------------------------------------------#
                # -----------------------tanks-------------------------#
            list_of_tanks = []
            team_1_tanks = []
            team_2_tanks = []
            list_of_tank_fillers = []

            for member in member_list:
                if Main_Tank in member.roles:
                    list_of_tanks = list_of_tanks + [member]
            if len(list_of_tanks) < 4:  # what to do if there are less then 4 maintanks
                for member in member_list:
                    if Tank in member.roles:
                        list_of_tanks = list_of_tanks + [member]

                if len(list_of_tanks) < 4:
                    number1 = len(list_of_tanks)
                    number = 4 - number1
                    print(number1)
                    print(number)
                    list_of_fillers = []
                    while number != 0:
                        for member in member_list:
                            if DPS or Main_DPS in member.roles:
                                list_of_fillers = list_of_fillers + [member]
                        choice = random.choice(list_of_fillers)
                        list_of_tanks = list_of_tanks + [choice]
                        number -= 1
                        print(number)

                if list_of_tanks == 4:
                    choice1 = random.choice(list_of_tanks)
                    team_1_tanks = team_1_tanks + [choice1.mention]
                    await choice1.send("You're playing **TANK** for **TEAM 1**. The PUG took place at " + str(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    await choice1.move_to(team_1_vc)
                    list_of_tanks.remove(choice1)
                    member_list.remove(choice1)

                    choice2 = random.choice(list_of_tanks)
                    team_1_tanks = team_1_tanks + [choice2.mention]
                    await choice2.send("You're playing **TANK** for **TEAM 1**. The PUG took place at " + str(
                        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    await choice2.move_to(team_1_vc)
                    list_of_tanks.remove(choice2)
                    member_list.remove(choice2)

                    choice3 = random.choice(list_of_tanks)
                    team_2_tanks = team_2_tanks + [choice3.mention]
                    await choice3.send("You're playing **TANK** for **TEAM 2**. The PUG took place at " + str(
                        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    await choice3.move_to(team_2_vc)
                    list_of_tanks.remove(choice3)
                    member_list.remove(choice3)

                    choice4 = random.choice(list_of_tanks)
                    team_2_tanks = team_2_tanks + [choice4.mention]
                    await choice4.send("You're playing **TANK** for **TEAM 2**. The PUG took place at " + str(
                        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    await choice4.move_to(team_2_vc)
                    list_of_tanks.remove(choice4)
                    member_list.remove(choice4)

                while len(list_of_tanks) > 4:
                    choice1 = random.choice(list_of_tanks)
                    if Tank in choice1.roles:
                        list_of_tanks.remove(choice1)

            while len(list_of_tanks) > 4:
                choice1 = random.choice(list_of_tanks)
                list_of_tanks.remove(choice1)

            if len(list_of_tanks) == 4:
                choice1 = random.choice(list_of_tanks)
                team_1_tanks = team_1_tanks + [choice1.mention]
                await choice1.send("You're playing **TANK** for **TEAM 1**. The PUG took place at " + str(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                await choice1.move_to(team_1_vc)
                list_of_tanks.remove(choice1)
                member_list.remove(choice1)

                choice2 = random.choice(list_of_tanks)
                team_1_tanks = team_1_tanks + [choice2.mention]
                await choice2.send("You're playing **TANK** for **TEAM 1**. The PUG took place at " + str(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                await choice2.move_to(team_1_vc)
                list_of_tanks.remove(choice2)
                member_list.remove(choice2)

                choice3 = random.choice(list_of_tanks)
                team_2_tanks = team_2_tanks + [choice3.mention]
                await choice3.send("You're playing **TANK** for **TEAM 2**. The PUG took place at " + str(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                await choice3.move_to(team_2_vc)
                list_of_tanks.remove(choice3)
                member_list.remove(choice3)

                choice4 = random.choice(list_of_tanks)
                team_2_tanks = team_2_tanks + [choice4.mention]
                await choice4.send("You're playing **TANK** for **TEAM 2**. The PUG took place at " + str(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                await choice4.move_to(team_2_vc)
                list_of_tanks.remove(choice4)
                member_list.remove(choice4)


            # -----------------------------------------------------#
            # -----------------------DPS---------------------------#

            list_of_dps = []
            list_of_members_dps = member_list
            team_1_dps = []
            team_2_dps = []

            for member in member_list:
                if Main_DPS in member.roles:
                    list_of_dps = list_of_dps + [member]

            if len(list_of_dps) < 4:  # what to do if there are less then 4 maintanks
                for member in member_list:
                    if DPS in member.roles:
                        list_of_dps = list_of_dps + [member]

                if len(list_of_dps) < 4:
                    list_of_dps = member_list

                if len(list_of_dps) == 4:
                    choice1 = random.choice(list_of_dps)
                    team_1_dps = team_1_dps + [choice1.mention]
                    await choice1.send("You're playing **DPS** for **TEAM 1**. The PUG took place at " + str(
                        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    await choice1.move_to(team_1_vc)
                    list_of_dps.remove(choice1)

                    choice2 = random.choice(list_of_dps)
                    team_1_dps = team_1_dps + [choice2.mention]
                    await choice2.send("You're playing **DPS** for **TEAM 1**. The PUG took place at " + str(
                        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    await choice2.move_to(team_1_vc)
                    list_of_dps.remove(choice2)

                    choice3 = random.choice(list_of_dps)
                    team_2_dps = team_2_dps + [choice3.mention]
                    await choice3.send("You're playing **DPS** for **TEAM 2**. The PUG took place at " + str(
                        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    await choice3.move_to(team_2_vc)
                    list_of_dps.remove(choice3)

                    choice4 = random.choice(list_of_dps)
                    team_2_dps = team_2_dps + [choice4.mention]
                    await choice4.send("You're playing **DPS** for **TEAM 2**. The PUG took place at " + str(
                        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    await choice4.move_to(team_2_vc)
                    list_of_dps.remove(choice4)

                while len(list_of_dps) > 4:
                    choice1 = random.choice(list_of_dps)
                    if DPS in choice1.roles:
                        list_of_dps.remove(choice1)

            while len(list_of_dps) > 4:
                choice1 = random.choice(list_of_dps)
                list_of_dps.remove(choice1)

            if len(list_of_dps) == 4:
                choice1 = random.choice(list_of_dps)
                team_1_dps = team_1_dps + [choice1.mention]
                await choice1.send("You're playing **DPS** for **TEAM 1**. The PUG took place at " + str(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                await choice1.move_to(team_1_vc)

                choice2 = random.choice(list_of_dps)
                team_1_dps = team_1_dps + [choice2.mention]
                await choice2.send("You're playing **DPS** for **TEAM 1**. The PUG took place at " + str(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                await choice2.move_to(team_1_vc)

                choice3 = random.choice(list_of_dps)
                await choice3.send("You're playing **DPS** for **TEAM 2**. The PUG took place at " + str(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                team_2_dps = team_2_dps + [choice3.mention]
                await choice3.move_to(team_2_vc)

                choice4 = random.choice(list_of_dps)
                team_2_dps = team_2_dps + [choice4.mention]
                await choice4.send("You're playing **DPS** for **TEAM 2**. The PUG took place at " + str(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                await choice4.move_to(team_2_vc)

            print(member_list)
            embed2 = discord.Embed(
                title='These players did not get picked this time, but they will play in the next game: ',
                description=str(list_of_forced_players), colour=discord.Colour.orange()
            )
            embed = discord.Embed(
                title='**__Team 1:__**',
                colour=discord.Colour.blue()
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
            await ctx.send(embed=embed)
            await ctx.send(embed=embed1)
            if list_of_forced_players != []:
                await ctx.send(embed=embed2)

        else:
            await ctx.send("You're not a PUG Runner.")


@bot.command()
async def move(ctx):
    team_1_vc = discord.utils.get(ctx.guild.channels, id=546297542158057492)
    team_2_vc = discord.utils.get(ctx.guild.channels, id=546337215911952384)
    voice_channel = discord.utils.get(ctx.guild.channels, id=542042691811409973)
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
