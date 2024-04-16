import discord
from discord.ext import commands
import asyncio
import requests
import time
intents= discord.Intents.all()
timers = {}
start_times={}
time_seconds = {}
elapsed_time = {}
time_passed = {}

is_finished = False

def reset(ctx):
    elapsed_time[ctx.author.id] = 0
    start_times[ctx.author.id] = 0
    time_passed[ctx.author.id]= 0





bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()

async def sett(ctx, timer):  #1234m
    time_value =  int(timer[:-1])
    time_unit = timer[-1]
    start_times[ctx.author.id] = time.time()

    if time_unit == 's':
        time_seconds[ctx.author.id] = time_value
        if time_value == 1:        
            time_unit_show = "second"

        else:
            time_unit_show = "seconds"

    elif time_unit == 'm':
        time_seconds[ctx.author.id] = time_value*60
        if time_value == 1:        
            time_unit_show = "minute"

        else:
            time_unit_show = "minutes"

    elif time_unit == 'h':
        time_seconds[ctx.author.id] = time_value*60*60
        if time_value == 1:        
            time_unit_show = "hour"

        else:
            time_unit_show = "hours"
        
   
    elif time_unit == 'd':
        time_seconds[ctx.author.id] = time_value*86400
        if time_value == 1:        
            time_unit_show = "day"

        else:
            time_unit_show = "days"
    
    else:
        await ctx.send("There is no such unit")
       

    
    #await asyncio.sleep(time_seconds)
    #await ctx.send(f"{ctx.author.mention}, Your {time_value} {time_unit_show} timer is up. Thank you!")


    if ctx.author.id in timers:
         timers[ctx.author.id].append((ctx.message.created_at, time_seconds))
    else:
        timers[ctx.author.id] = [(ctx.message.created_at, time_seconds)]

    await ctx.send(f" {ctx.author.mention}, Timer is set for {time_value} {time_unit_show}.")
    await asyncio.sleep(time_seconds[ctx.author.id])
    await ctx.send(f"{ctx.author.mention}, Your {time_value} {time_unit_show} timer is up. Thank you!")
    timers[ctx.author.id].remove((ctx.message.created_at, time_seconds))
    is_finished = True
    reset(ctx)
    


@bot.command()
async def desc(ctx):
    await ctx.send("Hi, I am Itsuwi and jobless.")

@bot.command()
async def gojo(ctx):
    await ctx.send("He dead ;)")
    url = "https://tenor.com/view/gojo-rip-gojo-dead-satorou-gojo-satorou-gojo-gif-14980512591692681384"
    await ctx.send(url)

@bot.command()
async def status(ctx):
    if ctx.author.id in start_times and time_seconds:
        start_time = start_times[ctx.author.id]
        total_time = time_seconds[ctx.author.id]
        
    
    int(start_time)
    elapsed_time[ctx.author.id] = time.time()-start_time
    time_passed[ctx.author.id] = round (total_time-elapsed_time[ctx.author.id])
    if time_passed[ctx.author.id] == 0:
        reset(ctx)
    await ctx.send(f"{ctx.author.mention}, {round(elapsed_time[ctx.author.id])} seconds has passed. {time_passed[ctx.author.id]} remaining. ")

bot.run("MTIyOTY4MjI4NTY3NTI4NjUzOA.GRMwcF.1lbd8tASjsd9nKKBKb3jLKYIy-123MRSm4mGyA")

