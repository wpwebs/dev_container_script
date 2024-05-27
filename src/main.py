import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("application.log"),
        logging.StreamHandler()
    ]
)

def main():
    print('Hi!')
    logging.info("Starting application")
    # Your application logic here

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"Application failed: {e}", exc_info=True)
        exit(1)
