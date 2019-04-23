using System;
using System.Threading.Tasks;
using System.IO;
using Newtonsoft.Json.Linq;

namespace GLR_Updater {
   class Updater {
      private string dataPath = Environment.ExpandEnvironmentVariables("%localappdata%/GLR_Manager/");
      private string downloadURL = "https://github.com/ImaniiTy/GreenLuma-Reborn-Manager/releases/download/v{0}/GreenLuma.Reborn.Manager.zip";
      private string latestVersionString;
      public async Task IsUpdated() {
         try {
            this.latestVersionString = await Utils.GetLatest();
         } catch (Exception e) {
            return;
         }

         var configJSON = File.ReadAllText(dataPath + "config.json");
         var currentVersionString = (string) JObject.Parse(configJSON)["version"];
         var currentVersion = new Version(currentVersionString);
         var latestVersion = new Version(this.latestVersionString);
         
         if (currentVersion.CompareTo(latestVersion) < 0) {
            Console.WriteLine("Outdated");
            
            try {
               Utils.downloadFile(String.Format(this.downloadURL, this.latestVersionString));
               Utils.extractFile();
            } catch (Exception e) {
               Console.WriteLine("Error while downloading...");
               Console.WriteLine(e.StackTrace);
            }
            
         }
         
      }
   }


}
