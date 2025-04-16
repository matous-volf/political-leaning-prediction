use load_dotenv::load_dotenv;

load_dotenv!();

pub(crate) const DEEPL_API_KEY: &str = env!("DEEPL_API_KEY");
