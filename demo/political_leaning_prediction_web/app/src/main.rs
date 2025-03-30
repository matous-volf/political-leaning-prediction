mod components;
mod models;
mod route;
mod server;
mod views;

use crate::components::App;
#[cfg(feature = "server")]
use crate::server::dotenv;
use dioxus::logger::tracing::info;
use dioxus::prelude::*;

fn main() {
    // server_only!(
    //     info!("Running migrations.");
    //     migrations::run_migrations().expect("Failed to run migrations.");
    // );

    // info!("Setting the storage directory.");
    // dioxus_sdk::storage::set_dir!();

    info!("Launching the app.");
    LaunchBuilder::new()
        // .with_context(server_only!(database_connection::create_connection_pool()))
        .launch(App);
}
