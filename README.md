# OLS
![OLS Banner](assets/banner.svg)<br>
OLS (Open Linux Shell) is a toolkit of CLI utilities designed to make terminal workflows more predictable, logged, and pipeline-friendly.
### **Warning**

> Arch Linux is recommended for OLS because it's easy to set up.<br>
> We plan to use AUR and all scripts are set up on Arch.

## installation
```bash
bash <(curl -sSL https://raw.githubusercontent.com/artemkolba321-spec/OLS/main/install.sh)
```

everything is ready
## philosophy
1. **Everything must be logged**  
   - All actions are recorded, making it easy to spot errors (EE) and trace what happened.

2. **OLS is a friendly set of programs**  
   - Minimal unnecessary flags  
   - Clear and consistent helpers (`--help` and `hp`)  
   - Commands work intuitively, even for advanced workflows.

3. **Designed for pipelines**  
   - All tools are pipeline-friendly, allowing chaining of commands effortlessly.  
   - Supports standard Linux streams (stdin/stdout/stderr) for maximum flexibility.

4. **All packages are downloaded from the Internet.**
   - Packages are downloaded once and can be used offline afterwards.
   - predictability
   - the user learns once