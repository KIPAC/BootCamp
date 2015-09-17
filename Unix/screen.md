# GNU screen

When working on the remote server, sometimes you may want to be able to multitask without having new connections, or you may want to disconnect without losing your current working stage. The `screen` program is handy in these cases.

## Usages

Simply type `screen` to start a new screen session. Once you are in a screen session, you can type `ctrl+a d` to "detach" from the screen, and what you are doing in each screen will still alive even when you disconnect. To "reattach" to a screen, use `screen -r`. 

You can also start multiple screens to work on different tasks, and switching between them. See [this page](https://www.linode.com/docs/networking/ssh/using-the-terminal#gnu-screen) for some advanced usages.

## Notes

When connecting to Stanford/SLAC load-balanced servers, you can be assigned to different servers each time you log in. In this case, you cannot reattach to the previous screen session. You need to log in to the exact same server for screen to work properly. 
