import discord
from discord.ext import commands
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
    voice_channel = discord.utils.get(ctx.guild.channels, id=547108815435464717)
    team_1_vc = discord.utils.get(ctx.guild.channels, id=505023650202648577)
    team_2_vc = discord.utils.get(ctx.guild.channels, id=505023848425455616)
    member_list = voice_channel.members
    choice1 = discord.Member
    choice2 = discord.Member
    choice3 = discord.Member
    choice4 = discord.Member

    if len(member_list) < 12:
        # what to do if there are less then 12 people in the vc
        await ctx.send('Not Enough Members to start a PUG')

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

            for member in member_list:
                if Main_Support in member.roles:
                    list_of_supports = list_of_supports + [member]

            if len(list_of_supports) < 4:  # what to do if there are less then 4 maintanks
                for member in member_list:
                    if Support in member.roles:
                        list_of_supports = list_of_supports + [member]

                if len(list_of_supports) == 4:
                    choice1 = random.choice(list_of_supports)
                    team_1_supports = team_1_supports + [choice1.mention]
                    await choice1.send("You're playing SUPPORT for Team 1, at the PUG that took place in: ")
                    await choice1.send(datetime.datetime.now())
                    await choice1.move_to(team_1_vc)
                    print(choice1)
                    list_of_supports.remove(choice1)
                    member_list.remove(choice1)
                    choice2 = random.choice(list_of_supports)
                    team_1_supports = team_1_supports + [choice2.mention]
                    await choice2.send("You're playing SUPPORT for Team 1, at the PUG that took place in: ")
                    await choice2.send(datetime.datetime.now())
                    await choice2.move_to(team_1_vc)
                    print(choice2)
                    list_of_supports.remove(choice2)
                    member_list.remove(choice2)
                    choice3 = random.choice(list_of_supports)
                    team_2_supports = team_2_supports + [choice3.mention]
                    await choice3.send("You're playing SUPPORT for Team 2, at the PUG that took place in: ")
                    await choice3.send(datetime.datetime.now())
                    await choice3.move_to(team_2_vc)
                    print(choice3)
                    list_of_supports.remove(choice3)
                    member_list.remove(choice3)
                    choice4 = random.choice(list_of_supports)
                    team_2_supports = team_2_supports + [choice4.mention]
                    await choice4.send("You're playing SUPPORT for Team 2, at the PUG that took place in: ")
                    await choice4.send(datetime.datetime.now())
                    await choice4.move_to(team_2_vc)
                    print('here it is')
                    list_of_supports.remove(choice4)
                    member_list.remove(choice4)
                while len(list_of_supports) > 4:
                    choice1 = random.choice(list_of_supports)
                    if Support in choice1.roles:
                        print(choice1)
                        list_of_supports.remove(choice1)

            while len(list_of_supports) >= 5:
                choice1 = random.choice(list_of_supports)
                print(choice1)
                list_of_supports.remove(choice1)

            if len(list_of_supports) == 4:
                choice1 = random.choice(list_of_supports)
                team_1_supports = team_1_supports + [choice1.mention]
                await choice1.send("You're playing SUPPORT for Team 1, at the PUG that took place in: ")
                await choice1.send(datetime.datetime.now())
                await choice1.move_to(team_1_vc)
                print(choice1)
                list_of_supports.remove(choice1)
                member_list.remove(choice1)
                choice2 = random.choice(list_of_supports)
                team_1_supports = team_1_supports + [choice2.mention]
                await choice2.send("You're playing SUPPORT for Team 1, at the PUG that took place in: ")
                await choice2.send(datetime.datetime.now())
                await choice2.move_to(team_1_vc)
                print(choice2)
                list_of_supports.remove(choice2)
                member_list.remove(choice2)
                choice3 = random.choice(list_of_supports)
                team_2_supports = team_2_supports + [choice3.mention]
                await choice3.send("You're playing SUPPORT for Team 2, at the PUG that took place in: ")
                await choice3.send(datetime.datetime.now())
                await choice3.move_to(team_2_vc)
                print(choice3)
                list_of_supports.remove(choice3)
                member_list.remove(choice3)
                choice4 = random.choice(list_of_supports)
                team_2_supports = team_2_supports + [choice4.mention]
                await choice4.send("You're playing SUPPORT for Team 2, at the PUG that took place in: ")
                await choice4.send(datetime.datetime.now())
                await choice4.move_to(team_2_vc)
                print(choice4)
                list_of_supports.remove(choice4)
                member_list.remove(choice4)


            # -----------------------------------------------------#
            # -----------------------tanks-------------------------#
            list_of_tanks = []
            list_of_members_tank = member_list
            team_1_tanks = []
            team_2_tanks = []

            for member in member_list:
                if Main_Tank in member.roles:
                    list_of_tanks = list_of_tanks + [member]
            if len(list_of_tanks) < 4:  # what to do if there are less then 4 maintanks
                for member in member_list:
                    if Tank in member.roles:
                        list_of_tanks = list_of_tanks + [member]
                if len(list_of_tanks) == 4:
                    choice1 = random.choice(list_of_tanks)
                    team_1_tanks = team_1_tanks + [choice1.mention]
                    await choice1.send("You're playing TANK for Team 1, at the PUG that took place in: ")
                    await choice1.send(datetime.datetime.now())
                    await choice1.move_to(team_1_vc)
                    list_of_tanks.remove(choice1)
                    list_of_members_tank.remove(choice1)

                    choice2 = random.choice(list_of_tanks)
                    team_1_tanks = team_1_tanks + [choice2.mention]
                    await choice2.send("You're playing TANK for Team 1, at the PUG that took place in: ")
                    await choice2.send(datetime.datetime.now())
                    await choice2.move_to(team_1_vc)
                    list_of_tanks.remove(choice2)
                    list_of_members_tank.remove(choice2)

                    choice3 = random.choice(list_of_tanks)
                    team_2_tanks = team_2_tanks + [choice3.mention]
                    await choice3.send("You're playing TANK for Team 2, at the PUG that took place in: ")
                    await choice3.send(datetime.datetime.now())
                    await choice3.move_to(team_2_vc)
                    list_of_tanks.remove(choice3)
                    list_of_members_tank.remove(choice3)

                    choice4 = random.choice(list_of_tanks)
                    team_2_tanks = team_2_tanks + [choice4.mention]
                    await choice4.send("You're playing TANK for Team 2, at the PUG that took place in: ")
                    await choice4.send(datetime.datetime.now())
                    await choice4.move_to(team_2_vc)
                    list_of_tanks.remove(choice4)
                    list_of_members_tank.remove(choice4)
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
                await choice1.send("You're playing TANK for Team 1, at the PUG that took place in: ")
                await choice1.send(datetime.datetime.now())
                await choice1.move_to(team_1_vc)
                list_of_tanks.remove(choice1)
                list_of_members_tank.remove(choice1)

                choice2 = random.choice(list_of_tanks)
                team_1_tanks = team_1_tanks + [choice2.mention]
                await choice2.send("You're playing TANK for Team 1, at the PUG that took place in: ")
                await choice2.send(datetime.datetime.now())
                await choice2.move_to(team_1_vc)
                list_of_tanks.remove(choice2)
                list_of_members_tank.remove(choice2)

                choice3 = random.choice(list_of_tanks)
                team_2_tanks = team_2_tanks + [choice3.mention]
                await choice3.send("You're playing TANK for Team 2, at the PUG that took place in: ")
                await choice3.send(datetime.datetime.now())
                await choice3.move_to(team_2_vc)
                list_of_tanks.remove(choice3)
                list_of_members_tank.remove(choice3)

                choice4 = random.choice(list_of_tanks)
                team_2_tanks = team_2_tanks + [choice4.mention]
                await choice4.send("You're playing TANK for Team 2, at the PUG that took place in: ")
                await choice4.send(datetime.datetime.now())
                await choice4.move_to(team_2_vc)
                list_of_tanks.remove(choice4)
                list_of_members_tank.remove(choice4)



            member_list = list_of_members_tank

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
                    if list_of_members_dps != []:
                        list_of_dps = list_of_members_dps

                if len(list_of_dps) == 4:
                    choice1 = random.choice(list_of_dps)
                    team_1_dps = team_1_dps + [choice1.mention]
                    await choice1.send("You're playing DPS for Team 1, at the PUG that took place in: ")
                    await choice1.send(datetime.datetime.now())
                    await choice1.move_to(team_1_vc)
                    list_of_dps.remove(choice1)
                    list_of_members_dps.remove(choice1)

                    choice2 = random.choice(list_of_dps)
                    team_1_dps = team_1_dps + [choice2.mention]
                    await choice2.send("You're playing DPS for Team 1, at the PUG that took place in: ")
                    await choice2.send(datetime.datetime.now())
                    await choice2.move_to(team_1_vc)
                    list_of_dps.remove(choice2)
                    list_of_members_dps.remove(choice2)

                    choice3 = random.choice(list_of_dps)
                    team_2_dps = team_2_dps + [choice3.mention]
                    await choice3.send("You're playing DPS for Team 2, at the PUG that took place in: ")
                    await choice3.send(datetime.datetime.now())
                    await choice3.move_to(team_2_vc)
                    list_of_dps.remove(choice3)
                    list_of_members_dps.remove(choice3)

                    choice4 = random.choice(list_of_dps)
                    team_2_dps = team_2_dps + [choice4.mention]
                    await choice4.send("You're playing DPS for Team 2, at the PUG that took place in: ")
                    await choice4.send(datetime.datetime.now())
                    await choice4.move_to(team_2_vc)
                    list_of_dps.remove(choice4)
                    list_of_members_dps.remove(choice4)

                while len(list_of_dps) > 4:
                    choice1 = random.choice(list_of_dps)
                    if DPS in choice1.roles:
                        list_of_dps.remove(choice1)

            while len(list_of_dps) > 4:
                choice1 = random.choice(list_of_dps)
                list_of_dps.remove(choice1)

            if len(list_of_dps) < 4:
                if member_list != []:
                    list_of_dps.remove(member_list)
                    list_of_dps = list_of_members_dps

            if len(list_of_dps) == 4:
                choice1 = random.choice(list_of_dps)
                team_1_dps = team_1_dps + [choice1.mention]
                await choice1.send("You're playing DPS for Team 1, at the PUG that took place in: ")
                await choice1.send(datetime.datetime.now())
                await choice1.move_to(team_1_vc)
                list_of_members_dps.remove(choice1)
                list_of_dps.remove(choice1)

                choice2 = random.choice(list_of_dps)
                team_1_dps = team_1_dps + [choice2.mention]
                await choice2.send("You're playing DPS for Team 1, at the PUG that took place in: ")
                await choice2.send(datetime.datetime.now())
                await choice2.move_to(team_1_vc)
                list_of_dps.remove(choice2)
                list_of_members_dps.remove(choice2)

                choice3 = random.choice(list_of_dps)
                team_2_dps = team_2_dps + [choice3.mention]
                await choice3.send("You're playing DPS for Team 2, at the PUG that took place in: ")
                await choice3.send(datetime.datetime.now())
                await choice3.move_to(team_2_vc)
                list_of_members_dps.remove(choice3)
                list_of_dps.remove(choice3)

                choice4 = random.choice(list_of_dps)
                team_2_dps = team_2_dps + [choice4.mention]
                await choice4.send("You're playing DPS for Team 2, at the PUG that took place in: ")
                await choice4.send(datetime.datetime.now())
                await choice4.move_to(team_2_vc)
                list_of_members_dps.remove(choice4)
                list_of_dps.remove(choice4)

            print(member_list)
            await ctx.send('```Team 1:```' + ' ```Supports```' + " " + str(team_1_supports) + '```Tanks```' + '' + str(
                team_1_tanks) + '```DPS```' + '' + str(team_1_dps))
            await ctx.send('```Team 2:```' + ' ```Supports```' + " " + str(team_2_supports) + '```Tanks```' + '' + str(
                team_2_tanks) + '```DPS```' + '' + str(team_2_dps))
            if list_of_forced_players != []:
                await ctx.send('```These members did not play this time, but they will play next time:```')
                await ctx.send(list_of_forced_players)

        else:
            await ctx.send("You're not a PUG Runner.")


@bot.command()
async def clear(ctx):
    team_1_vc = discord.utils.get(ctx.guild.channels, id=505023650202648577)
    team_2_vc = discord.utils.get(ctx.guild.channels, id=505023848425455616)
    voice_channel = discord.utils.get(ctx.guild.channels, id=547108815435464717)
    list_of_members_t1 = team_1_vc.members
    list_of_members_t2 = team_2_vc.members
    list_of_members = list_of_members_t1 + list_of_members_t2
    while len(list_of_members) != 0:
        choice1 = random.choice(list_of_members)
        await choice1.move_to(voice_channel)
        list_of_members.remove(choice1)
    print('all donezo!')


bot.run(token)

