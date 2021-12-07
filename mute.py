import discord 
from discord.ext import commands

token = 'REPLACE YOUR BOT TOKEN WITH THIS TEXT'

client = commands.Bot(command_prefix='?')

@client.command() # Mute command (Use this code if you want to handle more than 1 discord server with a single bot.)
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member:discord.Member):
    muted_role = discord.utils.get(ctx.guild.roles, name='muted' or 'Muted' or 'mute' or 'Mute')
    guild = ctx.guild
    if muted_role not in guild.roles:
        perm = discord.permissions(send_messages=False)
        await guild.create_role('Muted', permissions=perm)
        await member.add_roles((muted_role))
        embed = discord.Embed(title = f':mute: ``{member}`` was muted')
        await ctx.send(embed=embed)
        await ctx.message.delete()
    else:
        await member.add_roles(muted_role)
        embed = discord.Embed(title = f':mute: ``{member}`` was muted')
        await ctx.send(embed=embed)
        await ctx.message.delete()

@client.command() #unmute command
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member:discord.Member):
    muted_role = discord.utils.get(ctx.guild.roles, name='muted' or 'Muted' or 'mute' or 'Mute')
    await member.remove_roles(muted_role)
    embed = discord.Embed(title = f':white_check_mark: ``{member}`` was Unmuted')
    await ctx.send(embed=embed)  
    await ctx.message.delete() 
    #=====================================================================================================================================================================
    
  @client.command(aliases=['m']) #mute command (use this code if you want to hancle 1 discord server.) for local server 
# @commands.has_permissions(kick_members = True)
async def mute(ctx,member : discord.Member):  
    muted_role = ctx.guild.get_role() # paste your mute role

    await member.add_roles(muted_role)

    await ctx.send(member.mention +" Has been muted!")
    # embed = discord.Embed(title = f'``{member}`` was muted', description = ' ')
    # await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command(aliases=['unm']) #unmute
# @commands.has_permissions(kick_members = True)
async def unmute(ctx,member : discord.Member):
    muted_role = ctx.guild.get_role(893719706907840532)

    await member.remove_roles(muted_role)

    await ctx.send(member.mention +" Has been unmuted!")
    await ctx.message.delete()
    #=======================================================================================================================================================================
    
    client.run(token) # token register
