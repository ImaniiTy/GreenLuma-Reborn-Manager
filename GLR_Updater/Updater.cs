using System;
using System.Threading.Tasks;
using System.IO;
using System.Net.Http;
using System.Net;
using System.Diagnostics;
using Newtonsoft.Json.Linq;

namespace GLR_Updater {
   class Updater {
      private string dataPath = Environment.ExpandEnvironmentVariables("%localappdata%/GLR_Manager/");
      private string downloadURL = "https://github.com/ImaniiTy/GreenLuma-Reborn-Manager/releases/download/v{0}/GreenLuma.Reborn.Manager.zip";
      private string latestVersionString;
      private string currentVersionString;
      private StreamWriter logger = Utils.CreateLogger();
      public async Task IsUpdated() {
         try {
            this.latestVersionString = await Utils.GetLatest();
         } catch (Exception e) {
            PrintError(e.StackTrace, "Error while trying to get the last version.");
            return;
         }

         try {
            var configJSON = File.ReadAllText(dataPath + "config.json");
            this.currentVersionString = (string)JObject.Parse(configJSON)["version"];
         } catch (Exception e) {
            return;
         }

         var currentVersion = new Version(this.currentVersionString);
         var latestVersion = new Version(this.latestVersionString);
         
         if (currentVersion.CompareTo(latestVersion) < 0) {
            Console.WriteLine("Outdated");
            
            foreach (var process in Process.GetProcessesByName("GreenLuma Reborn Manager")) {
               if(!process.HasExited) {
                  process.Kill();
               }
            }

            while (Process.GetProcessesByName("GreenLuma Reborn Manager").Length > 0) {
               System.Threading.Thread.Sleep(500);
            }

            try {
               Console.WriteLine("Downloading Latest Version...");
               await Utils.DownloadAndExtractFile(String.Format(this.downloadURL, this.latestVersionString));
            } catch (WebException e) {
               PrintError(e.StackTrace, "Error while downloading.");
            } catch (Exception e) {
               PrintError(e.StackTrace, "Error while extracting.");
            }
            
         } else {
            Console.WriteLine("The Program is Up to date");
         }
         
      }

      private void PrintError(string stack, string mesage) {
         Console.WriteLine(mesage);
         this.logger.WriteLine(stack);

         Console.WriteLine("Press any key to close...");
         Console.ReadLine();
      }
   }


}
