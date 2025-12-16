import uvicorn

def main():
    uvicorn.run("src.ability_yug.main:app", reload=True)

if __name__ == "__main__":
    main()
