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
    voice_channel = discord.utils.get(ctx.guild.channels, id=542042691811409973)
    team_1_vc = discord.utils.get(ctx.guild.channels, id=546297542158057492)
    team_2_vc = discord.utils.get(ctx.guild.channels, id=546337215911952384)
    member_list1 = voice_channel.members
    Pug_Runner = discord.utils.get(ctx.guild.roles, name="PUG Runner")

    list_of_forced_players = []
    if len(member_list1) < 12:
        message = await ctx.send('Not enough members to start a PUG.')
        await asyncio.sleep(10)
        await message.delete
    while len(member_list1) > 12:
        choice = random.choice(member_list1)
        if choice not in list_of_forced_players:
            list_of_forced_players = list_of_forced_players + [choice.mention]
            member_list1.remove(choice)

    if len(member_list1) == 12:
        if Pug_Runner in ctx.author.roles:
            async def startup(difference):
                voice_channel = discord.utils.get(ctx.guild.channels, id=542042691811409973)
                team_1_vc = discord.utils.get(ctx.guild.channels, id=546297542158057492)
                team_2_vc = discord.utils.get(ctx.guild.channels, id=546337215911952384)
                member_list1 = voice_channel.members
                Main_DPS = discord.utils.get(ctx.guild.roles, name="DPS")
                DPS = discord.utils.get(ctx.guild.roles, name="Secondary - DPS")
                Tank = discord.utils.get(ctx.guild.roles, name="Secondary - Tank")
                Main_Tank = discord.utils.get(ctx.guild.roles, name="Tank")
                Main_Support = discord.utils.get(ctx.guild.roles, name="Support")
                Support = discord.utils.get(ctx.guild.roles, name="Secondary - Support")
                member_list = member_list1
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
                choices = [choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9, choice10,
                           choice11, choice12]
                list_of_supports = []
                team_1_supports = []
                team_2_supports = []

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

                    choice2 = random.choice(list_of_supports)
                    team_1_supports = team_1_supports + [choice2.mention]
                    member_list.remove(choice2)
                    list_of_supports.remove(choice2)

                    choice3 = random.choice(list_of_supports)
                    team_2_supports = team_2_supports + [choice3.mention]
                    member_list.remove(choice3)
                    list_of_supports.remove(choice3)

                    choice4 = random.choice(list_of_supports)
                    team_2_supports = team_2_supports + [choice4.mention]
                    member_list.remove(choice4)
                    list_of_supports.remove(choice4)

                if len(list_of_supports) < 4:
                    for member in member_list:
                        if Support in member.roles:
                            list_of_supports = list_of_supports + [member]
                    if len(list_of_supports) == 4:
                        choice1 = random.choice(list_of_supports)
                        team_1_supports = team_1_supports + [choice1.mention]
                        member_list.remove(choice1)
                        list_of_supports.remove(choice1)

                        choice2 = random.choice(list_of_supports)
                        team_1_supports = team_1_supports + [choice2.mention]
                        member_list.remove(choice2)
                        list_of_supports.remove(choice2)

                        choice3 = random.choice(list_of_supports)
                        team_2_supports = team_2_supports + [choice3.mention]
                        member_list.remove(choice3)
                        list_of_supports.remove(choice3)

                        choice4 = random.choice(list_of_supports)
                        team_2_supports = team_2_supports + [choice4.mention]
                        member_list.remove(choice4)
                        list_of_supports.remove(choice4)

                    while len(list_of_supports) > 4:
                        choice = random.choice(list_of_supports)
                        if Main_Support not in choice.roles:
                            list_of_supports.remove(choice)

                    if len(list_of_supports) == 3:
                        choice = random.choice(member_list)
                        print(len(list_of_supports))
                        list_of_supports = list_of_supports + [choice]

                    if len(list_of_supports) == 2:
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

                    if list_of_tanks == 4:
                        choice5 = random.choice(list_of_tanks)
                        team_1_tanks = team_1_tanks + [choice5.mention]
                        list_of_tanks.remove(choice5)
                        member_list.remove(choice5)

                        choice6 = random.choice(list_of_tanks)
                        team_1_tanks = team_1_tanks + [choice6.mention]
                        list_of_tanks.remove(choice6)
                        member_list.remove(choice6)

                        choice7 = random.choice(list_of_tanks)
                        team_2_tanks = team_2_tanks + [choice7.mention]
                        list_of_tanks.remove(choice7)
                        member_list.remove(choice7)

                        choice8 = random.choice(list_of_tanks)
                        team_2_tanks = team_2_tanks + [choice8.mention]
                        list_of_tanks.remove(choice8)
                        member_list.remove(choice8)

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

                    choice6 = random.choice(list_of_tanks)
                    team_1_tanks = team_1_tanks + [choice6.mention]
                    list_of_tanks.remove(choice6)
                    member_list.remove(choice6)

                    choice7 = random.choice(list_of_tanks)
                    team_2_tanks = team_2_tanks + [choice7.mention]
                    list_of_tanks.remove(choice7)
                    member_list.remove(choice7)

                    choice8 = random.choice(list_of_tanks)
                    team_2_tanks = team_2_tanks + [choice8.mention]
                    list_of_tanks.remove(choice8)
                    member_list.remove(choice8)

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

                    choice10 = random.choice(list_of_dps)
                    team_1_dps = team_1_dps + [choice10.mention]
                    list_of_dps.remove(choice10)

                    choice11 = random.choice(list_of_dps)
                    team_2_dps = team_2_dps + [choice11.mention]
                    list_of_dps.remove(choice11)

                    choice12 = random.choice(list_of_dps)
                    team_2_dps = team_2_dps + [choice12.mention]
                    list_of_dps.remove(list_of_dps)

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

                        choice10 = random.choice(list_of_dps)
                        team_1_dps = team_1_dps + [choice10.mention]
                        list_of_dps.remove(choice10)

                        choice11 = random.choice(list_of_dps)
                        team_2_dps = team_2_dps + [choice11.mention]
                        list_of_dps.remove(choice11)

                        choice12 = random.choice(list_of_dps)
                        team_2_dps = team_2_dps + [choice12.mention]
                        list_of_dps.remove(choice12)

                for member in member_list:
                    print(member.mention)

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

